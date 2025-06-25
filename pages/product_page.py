"""
Page Object class for single product page.
"""

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Product page functionality."""

    locators = ProductPageLocators()

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "Product name not found."

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            "Product price not found."

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message not found."

    def should_be_cart_total_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE), \
            'Total cart info message not found.'

    def add_to_cart(self):
        btn = self.browser.find_element(*self.locators.BTN_ADD_TO_CART)
        btn.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_product_in_added_success_message(self):
        self.should_be_success_message()
        msg = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)

        assert msg.is_displayed(), "Success message is not visible."
        assert product_name.text in msg.text, \
            "Product name does not match."

    def should_cart_total_msg_match_product_price(self):
        self.should_be_cart_total_message()
        msg = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)

        assert product_price.is_displayed(), "Product price not displayed."
        assert product_price.text in msg.text, "Cart total does not match to product price."
