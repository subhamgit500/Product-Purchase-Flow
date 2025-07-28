from pageObjects.login_logout import loginPage


def test_purchaseFlow(browserInstance):

    driver = browserInstance

    login = loginPage(driver)
    login.login()
    login.validateLogin()