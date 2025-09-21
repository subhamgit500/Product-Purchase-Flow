import time

from selenium.webdriver.common.by import By

import logging

from pageObjects.contact_us_page import ContactUs


logger = logging.getLogger(__name__)



class CartPage:

    popup_element = (By.XPATH, "//div[@class='modal-content']")
    item_added_message_element = (By.XPATH, "div/p[1]")
    viewcart_popup_element = (By.XPATH, "div/p[2]")
    remove_button_element = (By.CSS_SELECTOR, ".fa-times")
    continue_shopping_element = (By.XPATH, "div[3]/button")
    select_quantity_element = (By.ID, "quantity")
    proceed_to_checkout_element = (By.CSS_SELECTOR, "a[class*='check_out']")
    billing_address_element = (By.ID, "address_invoice")


    def __init__(self,driver):
        self.driver = driver


    def add_to_cart_and_verify(self):

        self.driver.find_element(By.CSS_SELECTOR, ".cart").click()  # click on Add to cart
        time.sleep(2)  # wait till popup appear
        viewcart_popup = self.driver.find_element(*self.popup_element)  # popup web element
        # verify pop up appear on the screen
        assert viewcart_popup.is_displayed(), "Failed to verify view cart pop up."
        logger.info("Successfully pop up appeared on the screen after clicking on Add to cart.")
        #get text for product is added
        item_added_message = viewcart_popup.find_element(*self.item_added_message_element).text
        # verify product is added to the cart
        assert "product has been added to cart." in item_added_message
        logger.info("Successfully product added to cart.")
        # click on view cart
        viewcart_popup.find_element(*self.viewcart_popup_element).click()
        time.sleep(2)

    def remove_product_and_re_add(self,product_quantity):

        # remove all products from cart if
        remove_buttons = self.driver.find_elements(*self.remove_button_element)
        for remove_button in remove_buttons:
            remove_button.click()
            logger.info("clicked on remove button.")
            time.sleep(1)
        logger.info("Successfully removed all products from cart.")

        self.driver.back()
        time.sleep(1)
        # click on Continue shopping (if pop up is still present)
        viewcart_popup = self.driver.find_element(*self.popup_element)  # popup web element
        continue_shopping = viewcart_popup.find_element(*self.continue_shopping_element)
        if continue_shopping.is_displayed():
            continue_shopping.click()
            time.sleep(1)

        # Enter quantity
        select_quantity = self.driver.find_element(*self.select_quantity_element)
        select_quantity.clear()
        select_quantity.send_keys(product_quantity)
        time.sleep(1)
        logger.info("Successfully product quantity updated.")

    def click_proceed_to_checkout(self):

        #click on Proceed To Checkout button
        proceed_to_checkout = self.driver.find_element(*self.proceed_to_checkout_element)
        if proceed_to_checkout.is_displayed():
            proceed_to_checkout.click()
            logger.info("Successfully clicked on Proceed To Checkout button.")
            time.sleep(2)

    def verify_billing_address(self, address_to_verify):

        billing_address = self.driver.find_element(*self.billing_address_element)
        assert address_to_verify in billing_address.text, "Expected and Actual billing address did not match."
        logger.info("Successfully verified billing address.")
        time.sleep(1)


    def go_to_contact_us(self):
        return ContactUs(self.driver)