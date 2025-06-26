"""
Page Object class for main page.
"""

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """Main page functionality."""

    locators = MainPageLocators()
