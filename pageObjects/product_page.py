import time
from time import sleep

from selenium.webdriver.common.by import By
import logging
logger = logging.getLogger(__name__)

class ProductPage:
    def __init__(self,driver):  #pass only driver to the constructor
        self.driver = driver
        self.product_btn = (By.XPATH, "//div[starts-with(@class,'shop-menu')]/ul/li[2]")
        self.search_bar = (By.CSS_SELECTOR, "#search_product")
        self.search_btn = (By.CSS_SELECTOR, "#submit_search")


    def search_and_view_product(self,str_search, str_category, str_product_category):

        filters = (By.XPATH, f"//a[contains(@href,'{str_category}')]")  #defining here because it is dynamic, need test data
        # /.. is used to go 1 step back to parent , instead of that we can use parent::
        product_category = (By.XPATH,f"//a[contains(@href,'{str_category}')]/../../../div/div/ul/li//a[contains(text(),'{str_product_category}')]")

        self.driver.find_element(*self.product_btn).click()  #click on product button
        time.sleep(1)
        logger.info("Successfully clicked on Product button.")

        #seach item
        self.driver.find_element(*self.search_bar).send_keys(str_search)  # Enter dress in Search bar
        self.driver.find_element(*self.search_btn).click()  # click search
        time.sleep(1)
        logger.info(f"{str_search} entered in search bar.")

        #select category
        filter = self.driver.find_element(*filters)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", filter)
        filter.click()
        time.sleep(1)
        logger.info(f"{str_category} selected successfully.")

        #select product category
        self.driver.find_element(*product_category).click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(1)
        logger.info(f"{str_product_category} selected successfully.")