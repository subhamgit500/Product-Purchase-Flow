from pageObjects.login_logout import loginPage


def test_purchaseFlow(browserInstance):

    driver = browserInstance

    loginLogout = loginPage(driver)
    loginLogout.login()
    loginLogout.validateLogin()

    loginLogout.logout()