"""
Locators for Page Object classes.
"""

from selenium.webdriver.common.by import By


class MainPageLocators:
    """Locators for MainPage class."""

    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
