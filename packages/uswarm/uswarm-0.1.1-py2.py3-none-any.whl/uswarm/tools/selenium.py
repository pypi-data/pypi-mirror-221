import time

from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#DRIVER = webdriver.Firefox
DRIVER = webdriver.Chrome

# def set_driver_factory(factory=webdriver.Firefox):
# nonlocal DRIVER_FACTORY
# DRIVER = factory

class WorkUnit:
    pass


class Browser(DRIVER):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    def find(self, xpath: str, timeout: int = 5, exception=False):
        t1 = time.time() + timeout
        while time.time() < t1:
            try:
                return self.find_element_by_xpath(xpath)
            except NoSuchElementException as why:  # if element isn't already loaded or doesn't exist
                # print(f"waiting for {xpath} ...")
                time.sleep(0.5)

        if exception:
            raise TimeoutError(f"Page loading timeout")  # or whatever the hell you want

    def findall(self, xpath: str, timeout: int = 12, exception=False):
        t1 = time.time() + timeout
        while True:
            try:
                return self.find_elements(by=By.XPATH, value=xpath)
                #return self.find_elements_by_xpath(xpath)
            except InvalidSelectorException as why:
                print(f"** ERROR: bad format: {xpath}")
                foo = 1
                if exception:
                    raise
            except NoSuchElementException as why:  # if element isn't already loaded or doesn't exist
                # print(f"waiting for {xpath} ...")
                if time.time() >= t1:
                    break
                time.sleep(0.5)



        if exception:
            raise TimeoutError(f"Page loading timeout")  # or whatever the hell you want


    def get(self, url, reload=False):
        if url:
            if reload or self.current_url!=url:
                super().get(url)