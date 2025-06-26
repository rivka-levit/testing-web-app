"""
Page Object class for single product page.
"""
import time
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
        # self.solve_quiz_and_get_code()  # Is needed to solve the course task

    def should_be_correct_product_in_success_message(self):
        msg_product_name = self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME
        ).text
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text

        assert product_name == msg_product_name, "Product name does not match."

    def should_match_cart_total_msg_to_product_price(self):
        message_cart_price = self.browser.find_element(
            *ProductPageLocators.CART_MESSAGE_PRICE
        ).text
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

        assert product_price == message_cart_price, ("Cart total does not match "
                                                     "to product price.")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be."

    def should_disappear_success_message(self):
        time.sleep(1)
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared."
