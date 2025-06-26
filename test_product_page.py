"""
Tests for product detail page.
"""

import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage

# LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

# Link to solve course task
# LINK = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

failed_links_numbers = [7]
links_to_check = [f'{LINK}?promo=offer{i}' if i not in failed_links_numbers else
                  pytest.param(
                      f'{LINK}?promo=offer{i}',
                      marks=pytest.mark.xfail
                  ) for i in range(0, 10)]




def test_product_info_is_visible(browser):
    """Test the product info is displayed correctly."""

    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_product_name()
    page.should_be_product_price()

# @pytest.mark.parametrize('link', links_to_check)
def test_guest_can_add_product_to_cart(browser):
    """Test that guest can add product to the cart."""

    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_cart()
    page.should_be_success_message()
    page.should_be_correct_product_in_success_message()
    page.should_be_cart_total_message()
    page.should_match_cart_total_msg_to_product_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Test there is no success message after adding product to the cart."""

    page = ProductPage(browser, LINK, timeout=None)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    """Test there is no success after opening product page."""

    page = ProductPage(browser, LINK, timeout=None)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Test the success message disappeared after adding product to the cart."""

    page = ProductPage(browser, LINK, timeout=None)
    page.open()
    page.add_to_cart()
    page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    """Test the login link is present on the product page."""

    link = ("http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
            "the-city-and-the-stars_95/")
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    """Test the guest can go to the login page."""

    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, LINK)
    login_page.should_be_login_page()
