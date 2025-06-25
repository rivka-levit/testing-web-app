"""
Base Page Object.
"""

from selenium.webdriver import Chrome, Firefox
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self,
                 browser: Chrome | Firefox,
                 url: str,
                 timeout: int=10) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by_attr, selector):
        try:
            self.browser.find_element(by_attr, selector)
        except NoSuchElementException:
            return False

        return True
