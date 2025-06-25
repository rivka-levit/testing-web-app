"""
Tests for product detail page.
"""

from pages.product_page import ProductPage

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

# Link to solve course task
# LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'


def test_product_info_is_visible(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_product_name()
    page.should_be_product_price()

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_cart()
    page.should_be_correct_product_in_added_success_message()
    page.should_cart_total_msg_match_product_price()
