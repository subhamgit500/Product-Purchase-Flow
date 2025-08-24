import time

from selenium.webdriver.common.by import By

from pageObjects.product_page import ProductPage
import logging
logger = logging.getLogger(__name__)

class LoginPage:

    def __init__(self,driver): #pass only driver to the constructor
        self.driver = driver
        self.signUploginButton = (By.CSS_SELECTOR,"a[href='/login']")
        self.email = (By.XPATH,"(//input[@name='email'])[1]")
        self.password = (By.CSS_SELECTOR,"input[name='password']")
        self.loginButton = (By.XPATH,"//button[text()='Login']")
        self.loggedIn = (By.XPATH,"//div[@class='shop-menu pull-right']/ul/li[10]/a")
        self.logoutButton = (By.XPATH,"//div[@class='shop-menu pull-right']/ul/li[4]/a")

    def verify_homepage_title_and_URL(self):

        title = self.driver.title
        getURL = self.driver.current_url
        logger.info(f"Title of the home page is {title}")
        logger.info(f"Url is {getURL}")

        #Verification
        assert title == "Automation Exercise"
        logger.info("Title verified successfully.")
        assert "https://automationexercise.com/" in getURL
        logger.info("URL verified successfully.")
        time.sleep(1)
        #scroll to verify page loaded fully
        self.driver.execute_script("window.scrollTo(0,1000)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,0)")
        logger.info("Page loaded successfully.")
        time.sleep(1)

    def login(self,username,password):
        self.driver.find_element(*self.signUploginButton).click()    #click Login/Signup button
        time.sleep(1)
        #Enter registered email and password (from config).
        self.driver.find_element(*self.email).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.loginButton).click()
        logger.info("successfully clicked on Login button.")
        time.sleep(1)

    def validate_login(self):
        loggedIn = self.driver.find_element(*self.loggedIn).text
        logout = self.driver.find_element(*self.logoutButton).text
        logger.info(loggedIn)
        logger.info(f"{logout} button is visible.")
        #Verify Logged in as username is displayed.
        assert "Logged in" in loggedIn and "Logout" in logout
        logger.info("Successfully logged in.")

    def logout(self):
        self.driver.find_element(*self.logoutButton).click()
        logger.info("Successfully logged out.")
        time.sleep(1)

    def go_to_product_page(self):
        return ProductPage(self.driver)




