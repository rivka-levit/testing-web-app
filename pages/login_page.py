"""
Page Object class for login page.
"""

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Login page functionality."""

    locators = LoginPageLocators()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, \
            'Current url is wrong. It is not a login page url.'

    def should_be_login_form(self):
        assert self.is_element_present(*self.locators.LOGIN_FORM), \
            'Login form is not present.'

    def should_be_register_form(self):
        assert self.is_element_present(*self.locators.REGISTER_FORM), \
            'Register form is not present.'
