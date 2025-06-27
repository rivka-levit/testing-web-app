"""
Page Object class for single product page.
"""

from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    """Cart page functionality."""

    locators = CartPageLocators()

    def should_be_cart_item(self):
        assert self.is_element_present(*self.locators.CART_ITEM), \
            "Cart item was not found."

    def should_not_be_cart_item(self):
        assert self.is_not_element_present(*self.locators.CART_ITEM), \
            "Cart item is present but should not be."

    def should_be_cart_url(self):
        assert 'basket' in self.browser.current_url, \
            "Current url is wrong. It is not a cart page url."

    def should_be_empty_cart_text(self):
        assert self.is_element_present(*self.locators.EMPTY_CART_TEXT), \
            "Empty cart text was not found."
