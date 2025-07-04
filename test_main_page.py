import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import CartPage

LINK = "http://selenium1py.pythonanywhere.com/ru/"


@pytest.mark.guest_login
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, LINK)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, LINK)
    page.open()
    page.should_be_cart_link()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_url()
    cart_page.should_not_be_cart_item()
    cart_page.should_be_empty_cart_text()
