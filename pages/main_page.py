"""
Page Object class for main page.
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """Main page functionality."""

    def go_to_login_page(self):
        locator = MainPageLocators.LOGIN_LINK
        login_link = self.browser.find_element(*locator)
        login_link.click()

    def should_be_login_link(self):
        locator = MainPageLocators.LOGIN_LINK
        assert self.is_element_present(*locator), "Login link was not found."

    def is_element_present(self, by_attr, selector):
        try:
            self.browser.find_element(by_attr, selector)
        except NoSuchElementException:
            return False

        return True
