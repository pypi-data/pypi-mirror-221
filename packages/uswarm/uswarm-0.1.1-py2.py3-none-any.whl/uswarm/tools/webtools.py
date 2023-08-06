import arrow
import hashlib
import locale
import time
import os
import pickle
import random
import re
import threading
import types
import functools
import math

from collections import deque
from io import FileIO

from selenium import webdriver
from selenium.common.exceptions import *


from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.errorhandler import WebDriverException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement

from uswarm.tools import soft, fileiter, best_score, get_calling_function, zip_like, parse_date_x
from uswarm.tools.selenium import *
from uswarm.tools.files import FSLock, IncrementalCSV, CSVFile
from uswarm.tools.containers import load_dataframes, rename_columns

from uswarm.tools.metrics import *

from uswarm.tools.webhelpers import (
    openfile,
    normalize_columns,
    TRX_MAP,
    parse_descriptor,
)

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger

log = logger(__name__)


# DRIVER = webdriver.Firefox
# from selenium.webdriver.firefox.options import Options
DRIVER = webdriver.Chrome
from selenium.webdriver.chrome.options import Options

# def set_driver_factory(factory=webdriver.Firefox):
# nonlocal DRIVER_FACTORY
# DRIVER = factory


class Browser(DRIVER):
    def __init__(self, options=None, *args, **kw):
        if not options:
            options = Options()
            options.add_argument("--headless")
        super().__init__(options=options)  # don't pass kw

    def find(self, xpath: str, timeout: int = 5, exception=True):
        t1 = time.time() + timeout
        while time.time() < t1:
            try:
                return self.find_element_by_xpath(xpath)
            except NoSuchElementException as why:  # if element isn't already loaded or doesn't exist
                # print(f"waiting for {xpath} ...")
                time.sleep(0.5)

        if exception:
            raise TimeoutError(f"Page loading timeout")  # or whatever the hell you want

    def findall(
        self, xpath: str, timeout: int = 15, exception=True, attempts=1, root=None
    ):
        root = root or self
        t1 = time.time() + timeout
        while time.time() < t1:
            try:
                for i in range(attempts):
                    result = root.find_elements(by=By.XPATH, value=xpath)
                    if result:
                        break
                    if i < attempts - 1:
                        time.sleep(0.2)
                return result
            except NoSuchElementException as why:  # if element isn't already loaded or doesn't exist
                # print(f"waiting for {xpath} ...")
                time.sleep(1)

        if exception:
            raise TimeoutError(f"Page loading timeout")  # or whatever the hell you want


class Action(dict):
    def __getitem__(self, key):
        return self.get(key, {})


ELEMENT_TEXT = {
    "input",
    "option",
}
ELEMENT_CLICK = {}

# REGEXP to parse an XPATHX
REG_XPATHX = """(?imux)
\.?//(?P<tag>[^\\[]+)
(
  \[
    @(?P<attr>\w+)
    [\s=]+
    ["']
    (?P<value>.*?)
    ["']
  \]
)?
$
"""

# extended properties to be include in a XPATHX
XPATHX_EXTRACTOR = {
    "role": "item.aria_role",
    "tag": "item.tag_name",
    "class": "item.get_dom_attribute('class')",
    "id": "item.get_dom_attribute('id')",
    "name": "item.get_dom_attribute('name')",
    "title": "item.get_dom_attribute('title')",
    "text": "item.text",
    "value": "item.get_dom_attribute('value')",
    "type": "item.get_attribute('type')",
    "rect": "item.rect",
}

GET_XVALUE = {
    "textbox": "item.text or item.get_dom_attribute('value')",
    "input": "item.text or item.get_dom_attribute('value')",
    "menuitem": "item.text",
}


def get_xprop(item, prop):
    expression = XPATHX_EXTRACTOR[prop]
    try:
        value = eval(expression)
        if value is None:
            value = ""
    except AttributeError:
        value = ""
    return value


def get_xtext(item):
    if isinstance(item, WebElement):
        if item.aria_role in ("combobox",):
            select = Select(item)
            return select.first_selected_option.text

        expression = GET_XVALUE.get(item.aria_role, "item.text")
        assert expression, "missing role in GET_XVALUE"
        return eval(expression)


class BrowserBot(Browser):
    URL = "https://xxx.xxx.es"
    URL_LOGING = "https://xxx.xx.es/password-login"

    T_LOGIN = {
        "user": "//input[@id='tlogin_email']",
        "password": "//input[@id='tlogin_password']",
        "_next": "//input[@name='login_submit']",
    }
    D_LOGIN = {
        "user": "xxx@gmail.com",
        "password": "xxx",
    }

    POLICY = [
        # ("dc.identifier", "w-"),  # overwrite, nop
        #("dc.identifier.other", "=n"),  # overwrite, nop
        #("dc.identifier", "=-"),  # overwrite, nop
        #("dc.coverage.spatial", "=-"),  # compare, nop
        #("dc.title", "=-"),  # compare, nop
        #("dc.description", "-n"),  # compare, nop
        #("dc.date.issued", "=n"),  # compare, add new
        #("dc.contributor.*", "=n"),  # compare, add new
        #("dc.subject", "-n"),  # compare, nop
        #("dc.format", "-n"),  # compare, nop
        #("dc.rigths.*", "--"),  # compare, nop
        #("dc.source", "-n"),  # compare, nop
        #("dc.type", "-n"),  # compare, nop
        #("dc.*", "--"),  # nop, add new
        #("iaph.provincia.*", "-n"),  # nop, add new
        #("iaph.disponibilidad.*", "-n"),  # nop, add new
        #("iaph.*", "--"),  # compare, nop
        #("image_file.*", "-u"),  # nop, upload new
        #("new.*", "-n"),  # nop, add new
    ]

    MISSING = {
    }


    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

        self.mapping = {}  #: columns mapping
        self.load_maps()

        self.page_handlers = {}
        self.page_blueprint = {}
        self._register_pages()

        self._windows_stack = deque()

        self.procedures = "proc"
        self._used = set()
        self._handler_cache = {}  #: match best function candidates

        self._cache = {}  #: web-element cache for fast extended properties

        # if getattr(self, 'HOME_URL', None):
        # self.get(self.HOME_URL)
        self._best_candidates = {}

        # human alike behavior
        self.typing_speed = 5
        self.org_typing_speed = self.typing_speed

        # factor of typing
        self.switch_webitem_factor = 2

        self.max_visual_locate_item_pause = 1
        self.check_eq_factor = 300*3



        self._dirty = False

    def switch_human_focus(self, n=2):
        """Simulate N an human switching n times his focus."""
        pause = random.random()*self.max_visual_locate_item_pause
        time.sleep(pause)

        freq = 1 / (1 + self.typing_speed * (1 + (2*random.random()-1)*0.25))
        #print(f"freq: {freq}")
        n = max(1, n)
        time.sleep(freq*n)
        return freq


    def click(self, item, pause=-1):
        """Isolate all *human* clicks in this method."""
        if pause < 0:
            pause = random.random()*self.max_visual_locate_item_pause

        log.verbose(f"waiting {pause:0.2f} secs before 'click' on item: {item.aria_role}")
        time.sleep(pause)
        item.click()

    def send_keys(self, item, value, clear=True):
        """Isolate all *human* writing in this method."""
        #pause = random.random()*self.max_visual_locate_item_pause
        #print(f"typing: {value}")
        if get_xtext(item) and clear:
            item.clear()

        freq = self.switch_human_focus()

        if True or random.randint(1, 10*len(value)) < 45:
            # its too long. Human would use Copy+Paste
            #freq = self.switch_human_focus(2)
            # and send all at once
            item.send_keys(value)
            return


        freq /= math.log10(3 + len(value))

        for char in value:
            freq /= (1.1 - (2*random.random()-1)*0.25)
            _char = char.upper()
            if _char < "0" or _char > "Z":
                # simulate "SHIFT"
                time.sleep(2*freq)
            #print(f" - freq: {freq}")
            item.send_keys(char)
            time.sleep(freq*random.random())

        # introduce typing "noise"
        if random.random() < 0.15:
            self.type_random_jump()

        factor = 1.1 if self.typing_speed < self.org_typing_speed else 0.99
        self.change_typing_speed(factor=factor, permanent=False)
        self.typing_speed=20

    def change_typing_speed(self, factor=2, permanent=True):
        self.typing_speed *= factor
        if permanent:
            self.org_typing_speed = self.typing_speed


    def type_random_jump(self):
        factor = 1 + 1.0*(random.random() - 0.5)
        self.org_typing_speed = self.typing_speed
        self.change_typing_speed(factor, permanent=False)


    def zoom(self, value="80%"):
        self.execute_script(f"document.body.style.zoom='{value}'")
        foo = 1


    def get_policy(self, _field_, **kw):

            # 1. action when field exists     : -|=|w
            #    -: do nothing
            #    =: check web and mem match
            #    w: overwrite web with mem

            # 2. action wheh field is missing : -|n
            #    -: do nothing
            #    =: check web and mem match
            #    n: add a new web-record and set (overwrite?) value

            # 3. action when checker fails    : -|x|X
            #    -: do nothing
            #    x: abort mem field edition (do not edit this field and move to next field)
            #    X: abort mem record edition (do not edit this record and move to next mem record)


            # get the default policy for this _field_
            for pattern, policy in self.POLICY:
                if re.match(pattern, _field_, re.I | re.DOTALL):
                    break
            else:
                policy = ""
            return policy

    def match(self, s_text, t_text, _keyword_=''):
        if not isinstance(s_text, str):
            s_text = str(s_text)
        if not isinstance(t_text, str):
            t_text = str(t_text)

        s_text = s_text.lower().strip()
        t_text = t_text.lower().strip()

        factor = self.check_eq_factor * (1 +random.random())
        pause = min(len(s_text), len(t_text)) / factor
        time.sleep(pause)

        if re.search(r"author|identifier|dc_coverage_spatial|provincia",_keyword_, re.I|re.DOTALL):
            s_text = set(re.findall("\w+", s_text))
            t_text = set(re.findall("\w+", t_text))

        elif re.search(r"dc_subject",_keyword_, re.I|re.DOTALL):
            # remove mising descriptors
            for missing in self.MISSING.get(_keyword_, []):
                s_text = s_text.replace(missing.lower(), "")

            s_text = set(re.findall("\w+", s_text))
            t_text = set(re.findall("\w+", t_text))
            # s_text.update(["bienes", "muebles"])

        elif re.search(r"dc_rights|dc_source",_keyword_, re.I|re.DOTALL):
            s_text = set(re.findall("\w+", s_text))
            t_text = set(re.findall("\w+", t_text))
            t_text.intersection_update(s_text)

        elif re.search(r"dc_title",_keyword_, re.I|re.DOTALL):
            s_text = set(re.findall("\w+", s_text))
            t_text = set(re.findall("\w+", t_text))
            return t_text.issubset(s_text) or s_text.issubset(t_text)

        #elif re.search(r"dc_date_.*",_keyword_, re.I|re.DOTALL):  # 1993 != 1993-01-01
            #try:
                #s_text = arrow.get(parse_date_x(s_text))
                #t_text = arrow.get(parse_date_x(t_text))
            #except Exception as why:
                #foo = 1

        elif _keyword_ in ("image_file", "filename"):
            s_text = os.path.basename(s_text)
            t_text = os.path.basename(t_text)

        return s_text == t_text


    def best_candidates(
        self, area, keyword, options, validator=".", cutter=r"[^.-_\W]+", samples=3
    ):  # TODO: use cache[area]
        return find_best_candidates(keyword, options, validator, cutter, samples)

    def push_window(self, item=None, wait=0.5, timeout=10):
        current_page = self.current_window_handle
        self._windows_stack.append(current_page)

        if item:
            old_wh = set(self.window_handles)
            self.click(item)
            time.sleep(wait)

            popup = set(self.window_handles).difference(old_wh)
            if popup:  # could be one o none more windows
                popup = popup.pop()
                self.switch_to.window(popup)
            else:
                log.info("action do not open a pop-window")

            return popup

    def pop_window(self, wait=0.5):
        last_page = self._windows_stack.pop()
        self.switch_to.window(last_page)
        time.sleep(wait)

    # register page handlers
    def handle(self, **ctx):
        """Handle current page based on data from context *ctx*.

        Special ctx keywords are:

        - "url"     : force browser to navitate to this page before interact with it.
        - "_action" : one or more actions (list) to apply with the same context.
                      Page can be changed during interaction i.e as a result of a final *click*
                      Next action will find a new page, and the process could move forward many times.


        Load and handle the page with registered methods."""
        results = {}
        url = ctx.get("url")
        url and self.get(url)
        time.sleep(0.1)
        # multiple handlers for same page maybe possible.
        # we need an extra argument to select the rigth one.
        actions = ctx.get("_action", ["default"])
        if not isinstance(actions, list):
            actions = [actions]
        for _action in actions:
            # refresh available handlers for te current page.
            # Note that page can change during previuos action interaction
            # So we need to recalc all available handler for every action we try to apply.
            handlers = self.find_page_handlers()
            if _action in handlers:
                handler = handlers[_action]  #: must exists
                log.verbose(f">> {handler.__func__.__name__:10}: {ctx}")
                ok = handler(**ctx)
                results[_action] = ok
                break
        else:
            print("-" * 60)
            print(f"** ERROR: _action='{_action}' is not registered for ")
            print(f"**      : '{self.current_url}' page")
            print(f"**      : I don't know what to do...")
            print("-" * 60)
            foo = 1
        return results

    def register_handler(
        self,
        blueprint,
        _action,
        handler,
    ):
        """Register a handler for a page.

        Page is checked seaching for all knonw blueprint marks.

        """
        assert isinstance(_action, str)
        key = hashlib.sha1(pickle.dumps(blueprint)).hexdigest()
        self.page_blueprint[key] = blueprint
        self.page_handlers.setdefault(key, {})[_action] = handler

    def unregister_handler(self, handler):
        """UnRegister a handler for a page.

        Page is checked seaching for all knonw blueprint marks.

        """
        raise NotImplementedError()

    def find_page_handlers(self):
        for attempt in range(5):
            scores = {}
            for key, blueprint in self.page_blueprint.items():
                score = 0
                for xpath in blueprint:
                    found = self.findall(xpath)
                    if found:
                        score += 1
                scores[key] = float(score) / len(blueprint)

            x = best_score(scores)
            log.verbose(f"- blueprints scores ----------------------")
            for key, score in scores.items():
                if x == key:
                    log.verbose(f"{key}: {score} << ")
                else:
                    log.verbose(f"{key}: {score}")

            key = best_score(scores)
            if scores[key] > 0.75:
                return self.page_handlers[key]

            log.warning(
                f"attemp: [{attempt}] : page blueprint is not clear... wait for any unload element..."
            )
            time.sleep(2)

        raise RuntimeError("you need to improve blueprints discrimination")

    def _register_pages(self):
        pass

    # fields names translations
    def load_maps(self):
        for path in fileiter(".", regexp="map.*fields\.(csv|xls|xlxs)"):
            df = openfile(path)
            for idx, row in df.iterrows():
                values = [x.strip().lower() for x in row.values]
                self.mapping[values[0]] = values[1]

    # web
    def needs_login(self):
        return False

    def login(self, **ctx):
        soft(ctx, role="admin")
        # cfg = self.load_config()
        # soft(ctx, **cfg)

        ## get the auth from login config
        # df = ctx["config"]
        # auth = df[df["role"] == ctx["role"]].iloc[0].to_dict()

        self.do(self.LOGIN["gather"], self.LOGIN["send"], **ctx)

        foo = 1

    def load_config(self, folder=None):
        if not folder:
            func = get_calling_function(level=2)
            folder = func.__func__.__name__

        return load_dataframes(
            kind=".*?", folder=folder, top=self.procedures, relative=True
        )

    def do(self, gather, send, **ctx):
        """Process in 2 steps:

        1- gather elements and data from page.
        2- apply values to this inputs control and activate links or buttons.

        """
        # struct = self.gather_elements(proc["gather"])
        send = dict(send)  # do not alter original one from outher-level.
        while True:
            env = dict(ctx)  # preserve a original copy of ctx
            env.update(send)
            soft(env, _next=True)

            struct = self.gather_elements_extended(gather)
            # data = {}
            # for key, items in struct.items():
            # data[key] = [item.text for item in items]
            # foo = 1
            try:
                changed = self.apply(struct, **env)
            except WebDriverException as why:
                if "id doesn't reference a Node" in why.msg:
                    # interface has chaged during apply
                    # retry with remain fields
                    # for k in self._used:
                    # send.pop(k)
                    print(f"pending: {self._used.difference(send)})")
                    continue
                else:
                    raise

            # print(f"{changed} elements applied.")
            break

    def gather_elements(self, template):
        struct = {}
        t1 = time.time() + 10
        for key, xpath in template.items():
            items = self.findall(xpath, exception=False)
            struct[key] = items
            if time.time() > t1:
                raise TimeoutException("xxxx xxx ...")

        return struct

    def gather_elements_extended(self, collector, root=None):
        """Try to gather data using a sort of extended XPATH.

        1. Locate all elements with same TAG, so we redice the search size.
        2. Detect which extended XPATHX properties are using (if any).
        3. Build a regexp based on parsed extended XPATHX.

        Exaple: "//input[@id='google']"
        d = {'tag': 'input', 'attr': 'id', 'value': 'google'}

        1. search all //input elements.
        2. get the extended 'attr' value evaluating the right *extractor* expression.
        3. build a regexp to match and extract any useful information to shape *keyword* holder.
        4. expand *keyword_exp* against *d* and set *keyword: value* in the result.
        """
        self._cache.clear()
        struct = {}

        def store_item(keyword, item):
            keyword = keyword.split(".")
            holder = struct
            last = keyword.pop()
            while keyword:
                holder = holder.setdefault(keyword.pop(0), {})
            holder[last] = item

        # exploring ALL elements in DOM can be expensive
        # so we do a partial parser or XPATH and apply some
        # regexp magic only with elements of XPATH type
        for keyword_exp, xpathx in collector:
            # detect if is a own custom xpathx using extended properties
            m = re.match(REG_XPATHX, xpathx)
            if m:
                # example {'tag': 'input', 'attr': 'id', 'value': 'google'}
                d = m.groupdict()
                tag = d["tag"]
                xpath = f"//{tag}"
            else:
                # print(f"can't parse extened XPATH {xpathx}")
                xpath = xpathx
                d = {}

            # use a local cache to avoid multiples drivers
            # searchs for same kind of elements
            if xpath not in self._cache:
                self._cache[xpath] = self.findall(xpath)

            # evaluate expressions to get the extended properties.
            # iterate over all (tag) elements to find which element
            # we need to extract the extended information
            for item in self._cache[xpath]:
                if d:  # is a xpathx extended property ?
                    prop = d["attr"]
                    value = get_xprop(item, prop)
                    # build a regexp to create a map for rendering keyword name
                    # print(d["value"])
                    m = re.search(d["value"], value, re.I | re.DOTALL | re.UNICODE)
                    if m:
                        d.update(m.groupdict(""))
                        keyword = keyword_exp.format_map(d)
                        # print(f" --1--> {xpathx} : {keyword}")
                        store_item(keyword, item)
                        # continue searching more elements (no break)
                else:
                    # add all items that match normal xpatch (not extended)
                    keyword = keyword_exp.format_map(d)
                    # print(f" --2--> {xpathx} : {keyword}")
                    store_item(keyword, item)
                foo = 1
        return struct

    def _HIDE_gather_elements_extended(self, collector, root=None):
        """Try to gather data using a sort of extended XPATH.

        1. Locate all elements with same TAG, so we redice the search size.
        2. Detect which extended XPATHX properties are using (if any).
        3. Build a regexp based on parsed extended XPATHX.

        Exaple: "//input[@id='google']"
        d = {'tag': 'input', 'attr': 'id', 'value': 'google'}

        1. search all //input elements.
        2. get the extended 'attr' value evaluating the right *extractor* expression.
        3. build a regexp to match and extract any useful information to shape *keyword* holder.
        4. expand *keyword_exp* against *d* and set *keyword: value* in the result.
        """
        self._cache.clear()
        struct = {}

        # exploring ALL elements in DOM can be expensive
        # so we do a partial parser or XPATH and apply some
        # regexp magic only with elements of XPATH type
        for keyword_exp, xpathx in collector:
            # detect if is a own custom xpathx using extended properties
            m = re.match(reg_xpathx, xpathx)
            if m:
                # example {'tag': 'input', 'attr': 'id', 'value': 'google'}
                d = m.groupdict()
                tag = d["tag"]
                xpath = f"//{tag}"
            else:
                # print(f"can't parse extened XPATH {xpathx}")
                xpath = xpathx
                d = {}

            # use a local cache to avoid multiples drivers
            # searchs for same kind of elements
            if xpath not in cache:
                cache[xpath] = self.findall(xpath)

            # evaluate expressions to get the extended properties.
            # iterate over all (tag) elements to find which element
            # we need to extract the extended information
            for item in cache[xpath]:
                if d:  # is a xpathx extended property ?
                    prop = d["attr"]
                    expression = extractor[prop]
                    try:
                        value = eval(expression)
                        if value is None:
                            value = ""
                    except AttributeError:
                        value = ""
                    # build a regexp to create a map for rendering keyword name
                    m = re.search(d["value"], value, re.I | re.DOTALL | re.UNICODE)
                    if m:
                        d.update(m.groupdict())
                        struct.setdefault(keyword_exp.format_map(d), []).append(item)
                else:
                    # add all items that match normal xpatch (not extended)
                    struct.setdefault(keyword_exp.format_map(d), []).append(item)
                foo = 1
        return struct

    def apply(self, struct, **data):
        """Try to apply data to found items in web page.

        1. resolve any *lookup-<field> popup window used to select the right field value
           (i.e selecting from a normalized list in another window or existing person name, etc)

        2. apply all visible value to items shown on this page.

        3. Values not yet applied may be applied in the next page when '_next' action is executed
           and the *filling* process continues.

        4. Elements are applied in reverse naming order, so '_xxx' keywords will be applied at the end.
           Other names order may not affect the filling procedure.
        """
        self._used = set()
        # lookup fields that will require a pop-up window to dive into and select the right field.
        for key, items in struct.items():
            m = re.match(r"(?P<lookup>(lookup|otracosa))-(?P<field>.*)", key)
            if m:
                # we have a lookup popup window for selecting field
                d = m.groupdict()
                field = d["field"]
                if field in data:
                    # we have data, so launch the lookup process
                    assert isinstance(
                        items, WebElement
                    )  # just 1 single botton, not a container

                    self.push_window(items)
                    # https://repositorio.iaph.es/tools/lookup.jsp?field=dc_contributor_author&formID=edit_metadata&valueInput=dc_contributor_author&authorityInput=dc_contributor_author_authority&collection=49bb2eb4-e1ef-4848-b99a-4d0f5280e504&isName=false&isRepeating=false&confIndicatorID=dc_contributor_author_confidence_indicator_id
                    self.handle(_value=data[field], **data)
                    # search results (just one)
                    self.pop_window()
                    self._used.add(field)

        # direct fields
        available = list(set(struct.keys()).intersection(data).difference(self._used))
        available.sort(reverse=True)

        changed = 0
        for key in available:
            items = struct[key]
            values = data[key]
            # if not isinstance(values, list):
            # values = list([values])

            for idx, value, item in zip_like(values, items):
                # for i, value in enumerate(values):
                # item = items[i]

                # build the handler name that will attend the item filling/action
                name_tokens = [
                    "",
                    "handle",
                ]  #: protected function that starts with '_handler_xxxxx'
                # add some tokens to the handler name
                item.tag_name and name_tokens.append(item.tag_name)
                item.aria_role and name_tokens.append(item.aria_role)
                item.get_attribute("type") and name_tokens.append(
                    item.get_attribute("type")
                )
                name = "_".join(name_tokens)

                # find and execute handler by name
                if name not in self._handler_cache:
                    # print(f"searching handler for: {name}")
                    # find the best function handler
                    candidates = {}
                    for func_name in dir(self):
                        if func_name.startswith("_handle_"):
                            func_tokens = func_name.split("_")
                            # match score
                            # for i in range(min(len(name_tokens), len(func_tokens))):
                            # if name_tokens[i] != func_tokens[i]:
                            # break
                            i = len(set(name_tokens).intersection(func_tokens))
                            candidates[func_name] = i  #: score

                    func_name = best_score(candidates)
                    self._handler_cache[name] = getattr(self, func_name)

                handler = self._handler_cache[name]

                changed += handler(item, value)
                # time.sleep(0.25)
            self._used.add(key)

        return changed

    def _handle_input_button_submit(self, item, value):
        """Handle items of type 'input'

        - value is string: send value as text.
        - value is bool = True: click on element.

        """
        if value:
            self.click(item)
            return True
        return False

    def _handle_select_combobox(self, item, value):
        """Handle items of type 'input'

        - value is string: send value as text.
        - value is bool = True: click on element.

        """
        select = Select(item)
        # foo = 1
        options = [x.get_attribute("value") for x in select.options]
        # values_mine = [t.strip() for t in item.text.splitlines()]
        # foo = 1
        values = [x.text for x in item.find_elements(By.XPATH, ".//option")]
        # assert values == values_mine # just check

        map_ = {k: values[i] for i, k in enumerate(options)}

        changed = 0
        if isinstance(value, (str,)):
            # search in keys or values
            matched = [k for k, v in map_.items() if value in k or value in v]
            l = len(matched)
            if l > 1 and not select.is_multiple:
                raise RuntimeError(
                    f"ERROR: multiple options match combobox but is not set as 'multiple': {matched}"
                )
            elif l == 0:
                raise RuntimeError(f"ERROR: '{value}' is not in '{values}'")

            for _value in matched:
                for op in select.all_selected_options:
                    if op.get_attribute("value") == _value:
                        # skip 'touch' in iterface (don't fire js events)
                        break
                else:
                    select.select_by_value(_value)
                    changed += 1
        else:
            print(f"value: {value} ??")
        return changed

    def _handle_menuitem(self, item, value):
        """Handle items of type 'input'"""
        if value:
            self.click(item)
            return True

        return False

    def _handle_input_textbox_text(self, item, value):
        """Handle items of type 'input'

        - value is string: send value as text.
        - value is bool = True: click on element.

        """
        if isinstance(value, (str, int, float)):
            _value = str(value)
            if _value != item.get_attribute("value"):
                self.send_keys(item, str(value), clear=True)
                return True
        else:
            print(f"** WARNING: _handle_textbox: value: {value} ({value.__class__}) ??")
        return False

    def _handle_input_none_file(self, item, value):
        """Handle items of type 'input'

        - value is string: send value as text.
        - value is bool = True: click on element.

        """
        if isinstance(value, (str, int, float)):
            _value = str(value)
            if _value != item.get_attribute("value"):
                self.send_keys(item, str(value), clear=True)
                return True
        else:
            print(f"** WARNING: _handle_textbox: value: {value} ({value.__class__}) ??")
        return False


class FSLock:
    def __init__(self, lock_file=None, grace: int = 40000):
        self.lock_file = lock_file or f"/tmp/lock-file.{time.perf_counter_ns()}.lock"
        self.grace = grace

        t1 = time.perf_counter_ns()
        self.unique = f"{t1} {os.getpid()}\n"

    def adquire_lock(self):
        lock_file = self.lock_file
        t1 = time.perf_counter_ns()
        unique = self.unique
        while True:
            try:
                existing = open(lock_file, "r").read()
                if existing != unique:
                    t0 = int(existing)
                    while True:
                        t1 = time.perf_counter_ns()
                        if t0 - t1 < 0:
                            print(f"force unlock")
                            break
                        time.sleep(random.random() * 0.1)
                else:
                    break  # lock adquire
            except FileNotFoundError as why:
                pass
            except Exception as why:
                time.sleep(random.random() * 0.1)

            t1 += self.grace  # 40 ms
            unique = f"{t1} {os.getpid()}\n"
            open(lock_file, "w").write(unique)

        # lock adquire
        self.unique = unique

    def release_lock(self):
        os.unlink(self.lock_file)


class IncrementalCSV(FileIO):

    order_idx_columns = ["id", "key"]
    order_field_columns = []
    sep = ", "

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.columns = []
        self.lock = FSLock(f"{self.name}.lock")

    def build_order_columns(self, keys):
        # has idx?
        keys = list(keys)
        for idx in set(self.order_idx_columns).intersection(keys):
            self.columns.append(idx)
            keys.remove(idx)

        assert self.columns, "No index has been defined!"

        # fields in same as preferece order_field_columns
        for idx in set(self.order_field_columns).intersection(keys):
            self.columns.append(idx)
            keys.remove(idx)

        # add the rest of the fields sorted by name
        keys.sort()
        self.columns.extend(keys)

    def write_record(self, record: dict):
        if not self.columns:
            self.build_order_columns(record.keys())

        line = self.sep.join([str(record[k]) for k in self.columns])
        line = bytes(f"{line}\n", "utf-8")
        try:
            self.lock.adquire_lock()
            self.write(line)
        finally:
            self.lock.release_lock()


def test_incremental_csv():
    filename = "/tmp/kk-incremental.csv"

    def greddy_writting(name, t1):

        t0 = time.time()
        time.sleep(t1 - t0)

        with IncrementalCSV(filename, mode="a") as f:
            for z in range(100):
                f.write_record({"id": 1, "name": name, "z": z})
            foo = 1

    t0 = time.time() + 2
    for i in range(10):
        name = f"greedy-{i}"
        th = threading.Thread(
            name=name, target=functools.partial(greddy_writting, name, t0)
        )
        th.start()

    while th.is_alive():
        time.sleep(1)

    print("-End-")


def extract_table(table, mapping, xpath=".//td", expression=None):
    """Create a record with data stored in a HTML table.
    - 1st row gives the header (keywords)
    - other rows are records
    """

    result = []
    header = {}
    for i, item in enumerate(table.find_elements(by=By.XPATH, value="//th")):
        text = item.text
        for pattern, keyword in mapping.items():
            if re.match(pattern, text, re.I | re.DOTALL):
                # print(f"{text} ---> {keyword}")
                header[i] = keyword
                break
        else:
            # print(f"ignoring keyword: {text}")
            pass

    for row in table.find_elements(by=By.XPATH, value=".//tr"):
        # print("-" * 80)
        record = {}
        for i, item in enumerate(row.find_elements(by=By.XPATH, value=xpath)):
            keyword = header.get(i)
            if keyword:
                value = item
                try:
                    if expression:
                        value = eval(expression)  # i.e. 'item.text'
                except Exception as why:
                    pass
                # print(f"- {keyword} : {value}")
                record[keyword] = value
        if record:
            result.append(record)
    return result


def extract_record(root, mapping, keys_xpath, values_xpath, expression=None):
    """Create a record with data stored in a HTML element root.
    - 1st row gives the header (keywords)
    - other rows are records
    """
    record = {}
    keys = root.find_elements(by=By.XPATH, value=keys_xpath)
    values = root.find_elements(by=By.XPATH, value=values_xpath)
    if len(keys) != len(values):
        print("Warning: keys and values have different lenghts")

    n = min(len(keys), len(values))

    for idx in range(n):
        item = keys[idx]
        # check if any keyword match in mapping
        string = item.text  # evaluate just once
        for pattern, key in mapping.items():
            m = re.match(pattern, string, re.I | re.DOTALL)
            if m:
                key = key.format_map(m.groupdict())
                break
        else:
            continue  # this key is not in mapping, skipping.

        item = values[idx]
        value = item
        try:
            if expression:
                value = eval(expression)  # i.e. 'item.text'
        except Exception as why:
            pass

        record[key] = value

    return record


def struct_2_record(struct):
    record = {}
    for key, item in struct.items():
        if isinstance(item, list):
            item = item[-1]
        record[key] = item.text
    return record


TOKEN_CUTTER = r"[^.-_\W]+"


def find_best_candidates(keyword, options, validator, cutter=TOKEN_CUTTER, samples=3):
    scores = {}

    _keyword1 = re.findall(cutter, keyword.lower())
    _keyword2 = "-".join(_keyword1)
    for option in options:
        if re.match(validator, option):
            _option1 = re.findall(cutter, option.lower())
            _option2 = "-".join(_option1)

            score = editDistDP(_keyword1, _option1) * 0.50
            score += distance(_keyword2, _option2) * 0.50

            while score in scores:
                score += 10**-6

            scores[score] = option

    _scores = list(scores)
    _scores.sort()
    return [(scores[x], x) for x in _scores[:samples]]


def find_best_record(result, ctx, **methods):
    """Find the best match using distance by default.
    Other methods can be specified per regexp-field.
    """
    brecord, bscore = None, (10**6)
    ascore = 0
    mscore = -bscore
    bidx = -1
    for idx, record in enumerate(result):
        score = 0
        for key, v0 in record.items():
            if key in ctx:
                v1 = str(ctx[key]).lower()
                v0 = str(v0).lower()

                d1 = distance(v0, v1)
                d1 += editDistDP(v0, v1)

                for pattern, meth in methods.items():
                    m = re.match(pattern, key, re.I | re.DOTALL)
                    if m:
                        d = m.groupdict()
                        soft(d, **ctx)
                        if isinstance(meth, str):  # assume is regexp
                            d["value"] = v1
                            meth = meth.format_map(d)
                            m = re.search(v1, v0, re.I | re.DOTALL)
                            if m:
                                d1 = 0
                                break
                score += d1
                foo = 1
        ascore += score
        if mscore < score:
            mscore = score

        if score < bscore:
            bidx, brecord, bscore = idx, record, score
    if result:
        ascore /= len(result)
    return bidx, brecord, bscore, ascore, mscore


if __name__ == "__main__":
    test_incremental_csv()
