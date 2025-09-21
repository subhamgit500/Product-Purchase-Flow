import time

from selenium.webdriver.common.by import By

import logging
logger = logging.getLogger(__name__)


class PlaceOrder:

    name_on_card = (By.NAME, "name_on_card")
    card_number = (By.NAME, "card_number")
    cvc = (By.NAME, "cvc")
    expiry_month = (By.NAME, "expiry_month")
    expiry_year = (By.NAME, "expiry_year")
    pay_and_confirm_btn = (By.ID, "submit")
    success_msg = (By.XPATH, "//p[contains(text(),'Congratulations')]")
    continue_btn = (By.XPATH, "//a[contains(text(),'Continue')]")

    def __init__(self,driver):
        self.driver = driver

    def payment(self):

        # click on - Place Order
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Place Order')]").click()
        time.sleep(1)
        # payment
        self.driver.find_element(*self.name_on_card).send_keys("John")
        self.driver.find_element(*self.card_number).send_keys("2345123467890989")
        self.driver.find_element(*self.cvc).send_keys("123")
        self.driver.find_element(*self.expiry_month).send_keys("05")
        self.driver.find_element(*self.expiry_year).send_keys("2025")
        # click on - Pay and Confirm Order
        self.driver.find_element(*self.pay_and_confirm_btn).click()
        time.sleep(2)

        order_confirm_message = self.driver.find_element(*self.success_msg).text
        assert "order has been confirmed" in order_confirm_message
        logger.info("Successfully order has been placed.")

        self.driver.find_element(*self.continue_btn).click()

        time.sleep(2)


