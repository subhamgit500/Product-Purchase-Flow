import time
from time import sleep

from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self,driver, str_category, str_product_category):
        self.driver = driver
        self.product_btn = (By.XPATH, "//div[starts-with(@class,'shop-menu')]/ul/li[2]")
        self.search_bar = (By.CSS_SELECTOR, "#search_product")
        self.search_btn = (By.CSS_SELECTOR, "#submit_search")
        self.filters = (By.XPATH, f"//a[contains(@href,'{str_category}')]")
        self.str_category = str_category  #to use it other methods
        self.str_product_category = str_product_category #to use it other methods
        # /.. is used to go 1 step back to parent , instead of that we can use parent::
        self.product_category = (By.XPATH,f"//a[contains(@href,'{str_category}')]/../../../div/div/ul/li//a[contains(text(),'{str_product_category}')]")


    def SearchAndViewProduct(self,str_search):
        self.driver.find_element(*self.product_btn).click()
        time.sleep(1)
        print("Successfully clicked on Product button.")

        #seach item
        self.driver.find_element(*self.search_bar).send_keys(str_search)  # Enter dress in Search bar
        self.driver.find_element(*self.search_btn).click()  # click search
        time.sleep(1)
        print(f"{str_search} entered in search bar.")

        #select category
        filter = self.driver.find_element(*self.filters)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", filter)
        filter.click()
        time.sleep(1)
        print(f"{self.str_category} selected successfully.")

        #select product category
        self.driver.find_element(*self.product_category).click()
        time.sleep(1)
        print(f"{self.str_product_category} selected successfully.")