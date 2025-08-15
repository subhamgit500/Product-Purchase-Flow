import time

from selenium.webdriver.common.by import By


class loginPage:

    def __init__(self,driver):
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
        print(f"Title of the home page is {title}")
        print(f"Url is {getURL}")

        #Verification
        assert title == "Automation Exercise"
        print("Title verified successfully.")
        assert "https://automationexercise.com/" in getURL
        print("URL verified successfully.")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        print("Page loaded successfully.")
        time.sleep(2)

    def login(self):
        self.driver.find_element(*self.signUploginButton).click()    #click Login/Signup button
        time.sleep(1)
        self.driver.find_element(*self.email).send_keys("johncena777@gmail.com")
        self.driver.find_element(*self.password).send_keys("JohnJohnCena@123")
        self.driver.find_element(*self.loginButton).click()
        time.sleep(2)

    def validateLogin(self):
        loggedIn = self.driver.find_element(*self.loggedIn).text
        logout = self.driver.find_element(*self.logoutButton).text
        print(loggedIn)
        print(f"{logout} button is visible.")
        assert "Logged in" in loggedIn and "Logout" in logout
        print("Successfully logged in.")



    def logout(self):
        self.driver.find_element(*self.logoutButton).click()
        print("Successfully logged out.")
        time.sleep(1)




