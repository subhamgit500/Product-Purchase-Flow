from pageObjects.login_logout import loginPage


def test_purchaseFlow(browserInstance):

    driver = browserInstance

    loginLogout = loginPage(driver)
    loginLogout.verify_homepage_title_and_URL()
    loginLogout.login()
    loginLogout.validateLogin()

    loginLogout.logout()