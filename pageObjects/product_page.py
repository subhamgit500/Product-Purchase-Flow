import time
from time import sleep

from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self,driver):
        self.driver = driver
        self.product_btn = (By.XPATH, "//div[starts-with(@class,'shop-menu')]/ul/li[2]")

    def SearchAndViewProduct(self):
        self.driver.find_element(*self.product_btn).click()
        time.sleep(1)
        print("Successfully clicked on Product button.")