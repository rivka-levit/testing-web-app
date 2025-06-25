"""
Page Object class for main page.
"""

from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """Main page functionality."""

    def __init__(self, browser, url):
        super().__init__(browser, url, locators_type=MainPageLocators)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*self.locators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*self.locators.LOGIN_LINK), \
            "Login link was not found."

    def is_element_present(self, by_attr, selector):
        try:
            self.browser.find_element(by_attr, selector)
        except NoSuchElementException:
            return False

        return True
