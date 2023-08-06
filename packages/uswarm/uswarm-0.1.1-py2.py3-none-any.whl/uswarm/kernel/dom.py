import os
import re

from uswarm.tools import (
    parse_uri,
    soft,
)

from .kernel import Resource, EVENT_IDLE, EVENT_SAVE, BASE_TIMER_EVENT

# from .stm import PSTM, MERGE_ADD, STATE_LIVE

# --------------------------------------------------
# Log
# --------------------------------------------------
from uswarm.tools.logs import logger
log = logger(__name__)


# ------------------------------------------
# Generic Filters
# ------------------------------------------
class Dict(dict):
    """A specialized *dict* with some filters implemented."""

    ORDER_KEYS = "date", "last_trade_date"

    def __getitem__(self, key):
        """Special"""
        if key not in self and isinstance(key, int):
            map_ = {}
            for k, v in self.items():
                for o in self.ORDER_KEYS:
                    if o in v:
                        map_[v[o]] = k, v
            keys = list(map_.keys())
            keys.sort()
            return map_[keys[0]]  # returns both k, v items

        return super().__getitem__(key)

    def over(self, key, value):
        """Filter items where key > value."""
        new = self.__class__()
        for k, item in self.items():
            if (key not in item) or (item[key] > value):
                new[k] = item
        return new

    def under(self, key, value):
        """Filter items where key < value."""
        new = self.__class__()
        for k, item in self.items():
            if (key not in item) or (item[key] < value):
                new[k] = item
        return new

    # def __getstate__(self):
    # return dict(self)

    # def __setstate__(self, item):
    # self.update(item)


class Dom(Dict):
    """A specialized *Dict* that acts like a Document Object Model (*DOM*).

    - xpath alike patching.
    - xpath alike get item.
    - find iterator similar to unix *find*.

    """
    

    re_param = re.compile(r"\{(?P<name>[^\}]*)\}")
    re_op = re.compile(r"(?P<op>[<>[=+*]+)(?P<name>[^/\]]*)")
    re_idx = re.compile(r"\[(?P<idx>(-|\w)+)\]")

    def _unroll(self, path, patch, dom, **env):
        """
        Get an elment from DOM

        - "{name}" : replace '{name}' by env replacement.
        - "={name}" : replace '{name}' by env replacement and don't split by '/' the result (urls typically)
        - ">name"  : replace 'dom' by dom[name] and insert in DOM
        - "<name"  : replace 'dom' by dom[name], breaking the descend, and doing nothing with DOM
        - "[name]" : index current dom (an items list) by item[key]

        Example: '/{path}/{symbol}/{local_symbol}/{timeframe}/>bars/[date]

        1. replace and go down using variable substitution: path, ..., timeframe.
        2. replace node by node['bars']. Next is a list of bars in this particular case.
        3. index each item in the current 'dom' (a list in this example) by its 'date' keyword value.

        Example: '/errors/{rid}/{date}'

        1. create 'errors' holder
        2. create a holder for 'rid' message/s.
        3. index by 'date'

        Note:

        - path and patch are join

        """
        assert os.path.isabs(path)
        env.update(dom)
        env["path"] = path

        # expand path
        aux = os.path.join(path, patch)
        aux = aux.split("/")

        # break down all path sublevels
        result = []
        retire = set([])
        setters = []
        while aux:
            setter = None
            name = aux.pop(0)
            # TODO : recursive param expansion
            # 1. expand name
            m = isinstance(name, str) and self.re_param.match(name)
            if m:
                (key,) = m.groups()
                if key in dom:
                    retire.add(key)
                    name = dom[key]
                else:
                    name = name.format(**env)

            # 2. operations (when apply)
            m = isinstance(name, str) and self.re_op.match(name)
            if m:
                operation, name = m.groups()
                for op in operation:
                    if op == ">":
                        # replace dom by dom[name]
                        dom = dom[name]
                        setters.append(name)
                        # and insert name in recursive dive-down keys
                        aux.insert(0, name)

                    elif op == "<":
                        # replace dom by dom[name]
                        dom = dom[name]
                        setters.append(name)
                        # do nothing and break the descend
                        break

                    elif op == "[":
                        # index list with key 'name'
                        # check if is a number(pos) or string(key)
                        try:
                            name = eval(name, env)
                            if isinstance(name, int):
                                pass
                            else:
                                raise RuntimeError(f"[{name}] ???-???", name)
                        except Exception as why:
                            foo = 1
                        setters.append(name)

                    elif op == "=":
                        # literal insertion
                        aux.insert(0, name)  # raw insert
                        name = None
                        break  # do not split '/' char
                    elif op == "+":
                        assert (
                            not name
                        ), "operator '+' takes no arguments, just append to the list"
                        if isinstance(l_v, dict) and not where:
                            where = l_v[l_k] = list()
                            where.append(dom)
                            assert (
                                not aux
                            ), "operator '+' should be the last one in xpath"
                            return

                    if name in setters:
                        continue

                    if isinstance(name, str):
                        spl = name.split("/")
                        if len(spl) > 1:
                            spl.extend(aux)
                            aux = spl
                            continue

            if name:
                if isinstance(name, str):
                    for k in name.split("/"):
                        if k and k not in result:
                            result.append(k)
                elif name not in result:
                    result.append(name)

        return result, retire, setters

    def g(self, path, **env):
        result, retire, setter = self._unroll(path, patch="", dom={}, **env)

        for key in retire:
            self.pop(key)

        holder = self
        for key in result:
            if isinstance(key, int) and isinstance(holder, dict):
                if holder:
                    keys = list(holder.keys())
                    keys.sort()  # TODO: review sorting keys before accessing
                    key = keys[key]
                else:
                    raise RuntimeError("Empty ??")
            holder = holder.setdefault(key, dict())
        return holder

    def patch(self, path, patch, dom, **env):
        """Update the dom with some data in somewhere
        pointed by patch.

        - "{name}" : replace '{name}' by env replacement.
        - "={name}" : replace '{name}' by env replacement and don't split by '/' the result (urls typically)
        - ">name"  : replace 'where' by dom[name]
        - "[name]" : index current dom (a list item) by item[key]
        - "+"      : replace current 'where' holder (dict) by list.
                     Following operation should be "append" not [index]

        Example: '/{path}/{symbol}/{local_symbol}/{timeframe}/>bars/[date]

        1. replace and go down using variable substitution: path, ..., timeframe
        2. replace dom by dom['bars']. Next is a list of bars
        3. index the 'dom' (a list) by 'date' key of each item.

        Example: '/errors/{rid}/{date}'

        1. create 'errors' holder
        2. create a holder for 'rid' message/s.
        3. index by 'date'

        """

        result, retire, setters = self._unroll(path, patch, dom, **env)
        # apply the keys that must be retired from dom
        # as they have been used.
        for key in retire:
            dom.pop(key, None)

        # create the down-path from '/' accross it-self.
        holder = self
        for key in result:
            holder = holder.setdefault(key, dict())

        # in case of having setters, we descend through dom but last key ...
        if setters:
            for key in setters[:-1]:
                dom = dom.get(key, dom)

            # ... and traslade the desired dom element to this (holder)
            name = setters[-1]
            for item in dom:
                key = item.pop(name)
                holder[key] = item
        else:
            # otherwise, we simply update the this (holder) leaf with remaining dom.
            holder.update(dom)

    def find(self, key_patt, value_patt="."):
        # vpattern = kw.get('vpattern', '.')

        # meta = '|'.join(patterns)
        # meta = re.compile(meta)
        # vpattern = re.compile(vpattern)

        for root, container in walk(
            self,
        ):
            path = "/".join([str(x) for x in root])
            m = re.search(key_patt, path)
            if m:
                d = m.groupdict()
                aux = str(container)
                m = re.search(value_patt, aux)
                if m:
                    d.update(m.groupdict())
                    yield path, container, d

    def subset(self, definition):
        res = self.__class__()
        for key_patt, patch in definition.items():
            for path, value, d in self.find(key_patt):
                dom = {}
                dom[d["key"]] = value
                res.patch("/", patch, dom, **d)

        return res

    # TODO: review
    # hooks / pub-sub
    def add_hook(self, hook, func, *args, **kw):
        # kw.setdefault("worker", self)
        if not hasattr(self, "_hooks"):
            self._hooks = {}

        self._hooks.setdefault(hook, list()).append(tuple([func, args, kw]))

    def _hook(self, hook, *args, **kw):
        for regexp, (func, args_, kw_) in self._hooks.items():
            if re.match(regexp, hook):
                _kw = dict(kw_)
                _kw.update(kw)
                _args = args or args_
                scall(func, *_args, **_kw)

    # saving support
    def __getstate__(self):
        return dict(self)

    def __setstate__(self, state):
        self.clear()
        self.update(state)


class DOM(Resource, Dom):
    KERNEL_URI_REGISTERING = "(dom)://"
    
    def __init__(self, uri, kernel, *args, **kw):
        super().__init__(uri, kernel, *args, **kw)
