"""
Base Page Object.
"""

from selenium.webdriver import Chrome, Firefox


class BasePage:
    def __init__(self,
                 browser: Chrome | Firefox,
                 url: str,
                 locators_type=None,
                 timeout: int=10) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

        if locators_type is None:
            self.locators = locators_type
        else:
            self.locators = locators_type()

    def open(self):
        self.browser.get(self.url)
