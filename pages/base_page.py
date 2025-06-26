"""
Base Page Object.
"""

import math

from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.support import expected_conditions as EC  # noqa
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (NoSuchElementException,
                                        NoAlertPresentException,
                                        TimeoutException)


class BasePage:
    def __init__(self,
                 browser: Chrome | Firefox,
                 url: str,
                 timeout: int = 10) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

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

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, poll_frequency=1).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True

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
