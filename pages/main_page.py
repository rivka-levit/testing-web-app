"""
Page Object class for main page.
"""

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """Main page functionality."""

    locators = MainPageLocators()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*self.locators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*self.locators.LOGIN_LINK), \
            "Login link was not found."
