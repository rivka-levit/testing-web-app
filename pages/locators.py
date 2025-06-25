"""
Locators for Page Object classes.
"""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Locators for MainPage class."""

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators :
    """Locators for LoginPage class."""

    # Login form locators
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_USER_NAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    BTN_LOGIN = (By.CSS_SELECTOR, "button[value='Log In']")

    # Registration form locators
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_1 = (By.ID, "registration-password1")
    REGISTER_PASSWORD_2 = (By.ID, "registration-password2")
    BTN_REGISTER = (By.CSS_SELECTOR, "button[value='Register']")
