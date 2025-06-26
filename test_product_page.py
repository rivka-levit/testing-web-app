"""
Tests for product detail page.
"""

import pytest

from pages.product_page import ProductPage

# LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'

failed_links_numbers = [7]

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
links_to_check = [f'{LINK}?promo=offer{i}' if i not in failed_links_numbers else
                  pytest.param(
                      f'{LINK}?promo=offer{i}',
                      marks=pytest.mark.xfail
                  ) for i in range(0, 10)]

# Link to solve course task
# LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


def test_product_info_is_visible(browser):
    """Test the product info is displayed correctly."""

    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_product_name()
    page.should_be_product_price()

@pytest.mark.parametrize('link', links_to_check)
def test_guest_can_add_product_to_cart(browser, link):
    """Test that guest can add product to the cart."""

    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_success_message()
    page.should_be_correct_product_in_success_message()
    page.should_be_cart_total_message()
    page.should_match_cart_total_msg_to_product_price()
