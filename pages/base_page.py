"""
Base Page Object.
"""

import math

from .locators import BasePageLocators

from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (NoSuchElementException,
                                        NoAlertPresentException,
                                        TimeoutException)


class BasePage:
    """Base Page Object."""

    locators = BasePageLocators()

    def __init__(self,
                 browser: Chrome | Firefox,
                 url: str,
                 timeout: int | None = 10) -> None:
        self.browser = browser
        self.url = url
        if timeout:
            self.browser.implicitly_wait(timeout)

    def go_to_cart_page(self):
        cart_link = self.browser.find_element(*self.locators.CART_LINK)
        cart_link.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*self.locators.LOGIN_LINK)
        login_link.click()

    def is_disappeared(self, by_attr, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, poll_frequency=1).until_not(
                EC.presence_of_element_located((by_attr, selector))
            )
        except TimeoutException:
            return False

        return True

    def is_element_present(self, by_attr, selector) -> bool:
        try:
            self.browser.find_element(by_attr, selector)
        except NoSuchElementException:
            return False

        return True

    def is_not_element_present(self, by_attr, selector) -> bool:
        try:
            WebDriverWait(self.browser, timeout=4).until(
                EC.presence_of_element_located((by_attr, selector))
            )
        except TimeoutException:
            return True

        return False

    def open(self):
        self.browser.get(self.url)

    def should_be_cart_link(self):
        assert self.is_element_present(*self.locators.CART_LINK), \
            "Cart link was not found."

    def should_be_login_link(self):
        assert self.is_element_present(*self.locators.LOGIN_LINK), \
            "Login link was not found."

    def solve_quiz_and_get_code(self):
        """Solve the quiz and get the code in the course task."""

        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
