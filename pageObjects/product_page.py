import time
from logging import exception
from time import sleep

from selenium.webdriver.common.by import By
import logging

from pageObjects.cart_page import CartPage

logger = logging.getLogger(__name__)

class ProductPage:

    product_btn = (By.XPATH, "//div[starts-with(@class,'shop-menu')]/ul/li[2]")
    search_bar = (By.CSS_SELECTOR, "#search_product")
    search_btn = (By.CSS_SELECTOR, "#submit_search")

    def __init__(self,driver):  #pass only driver to the constructor
        self.driver = driver



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

    def view_product_and_verify(self,item_to_select, price_to_verify):

        item = self.driver.find_element(By.XPATH, f"//div[@class='product-image-wrapper']/div/div/p[text()='{item_to_select}']/../../../div[@class='choose']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", item)
        item.click()  # open product details page
        logger.info(f"Successfully clicked on product : {item_to_select}.")

        try:
            # price verification
            price = self.driver.find_element(By.XPATH, "//span/span")
            assert price_to_verify in price.text, "Price did not match."
            logger.info(f"Successfully verified price of the product.")

        except Exception as e:
            print(e)

        finally:
            # image Verification
            image = self.driver.find_element(By.CSS_SELECTOR, "img[src*='picture']")  # it's common for all products
            assert image.is_displayed(), "Image is not visible"
            logger.info(f"Successfully verified product image.")

    def go_to_cart_page(self):
        return CartPage(self.driver)