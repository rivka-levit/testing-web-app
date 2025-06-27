"""
Locators for Page Object classes.
"""

from selenium.webdriver.common.by import By


class BasePageLocators:
    """Base class for Page Locators."""

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "header .page_inner a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators(BasePageLocators):
    """Locators for MainPage class."""


class LoginPageLocators(BasePageLocators):
    """Locators for LoginPage class."""

    # Login form locators
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_USER_NAME = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")
    BTN_LOGIN = (By.CSS_SELECTOR, "button[value='Log In']")

    # Registration form locators
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_2 = (By.ID, "id_registration-password2")
    BTN_REGISTER = (By.CSS_SELECTOR, "button[value='Register']")


class ProductPageLocators(BasePageLocators):
    """Locators for ProductPage class."""

    BTN_ADD_TO_CART = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-safe.alert-info")
    CART_MESSAGE_PRICE = (By.CSS_SELECTOR, ".alert-safe.alert-info .alertinner strong")


class CartPageLocators(BasePageLocators):
    """Locators for CartPage class."""

    CART_ITEM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_CART_TEXT = (By.CSS_SELECTOR, "#content_inner > p")