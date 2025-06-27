"""
Page Object class for login page.
"""

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Login page functionality."""

    locators = LoginPageLocators()

    def register_new_user(self, email, password):
        """Register new user."""

        email_input = self.browser.find_element(*self.locators.REGISTER_EMAIL)
        email_input.clear()
        email_input.send_keys(email)
        password_input_1 = self.browser.find_element(*self.locators.REGISTER_PASSWORD_1)
        password_input_1.clear()
        password_input_1.send_keys(password)
        password_input_2 = self.browser.find_element(*self.locators.REGISTER_PASSWORD_2)
        password_input_2.clear()
        password_input_2.send_keys(password)
        btn = self.browser.find_element(*self.locators.BTN_REGISTER)
        btn.click()

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
