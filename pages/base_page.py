"""
Base Page Object.
"""

from selenium.webdriver import Chrome, Firefox


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
