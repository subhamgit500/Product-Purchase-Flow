import time

from selenium.webdriver.common.by import By

import logging

from pageObjects.place_order import PlaceOrder

logger = logging.getLogger(__name__)




class ContactUs:

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    subject = (By.NAME, "subject")
    message = (By.ID, "message")
    upload_file = (By.NAME, "upload_file")
    submit = (By.NAME, "submit")
    cart= (By.XPATH, "//a[contains(text(),'Cart')]")
    proceed_to_checkout = (By.CSS_SELECTOR, "a[class*='check_out']")


    def __init__(self,driver):
        self.driver = driver

    def submit_feedback(self):

        self.driver.find_element(By.XPATH, "//a[contains(text(),'Contact us')]").click()

        self.driver.find_element(*self.name).send_keys("Sydney")
        self.driver.find_element(*self.email).send_keys("sydney.sweeny@baby.com")
        self.driver.find_element(*self.subject).send_keys("Good clothes")
        self.driver.find_element(*self.message).send_keys("Nice clothes, please add new collections")
        self.driver.find_element(*self.upload_file).send_keys("C:\\PythonProject\\Test_File_To_upload\\Feedback.txt")

        time.sleep(2)

        self.driver.find_element(*self.submit).click()
        time.sleep(1)
        self.driver.switch_to.alert.accept()  # click on Ok button in the alert popup
        time.sleep(2)
        message_post_feedback_submission = self.driver.find_element(By.CSS_SELECTOR, ".status.alert.alert-success").text
        assert "Your details have been submitted successfully" in message_post_feedback_submission
        logger.info("Details submitted successfully.")

    def click_cart_and_checkout(self):
        self.driver.find_element(*self.cart).click()
        time.sleep(2)
        logger.info("Successfully clicked on Cart.")
        self.driver.find_element(*self.proceed_to_checkout).click()
        time.sleep(2)
        logger.info("Successfully clicked on Proceed To Checkout button.")

    def go_to_place_order(self):
        return PlaceOrder(self.driver)
