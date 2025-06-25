"""
Page Object class for single product page.
"""

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Product page functionality."""

    locators = ProductPageLocators()

    def add_to_cart(self):
        btn = self.browser.find_element(*self.locators.BTN_ADD_TO_CART)
        btn.click()
