import json

import pytest

from pageObjects.login_logout import loginPage

#retrive test data
with open("C:\\PythonProject\\ProductPurchaseFlow\\utilities\\test_data.json") as file:
    test_dict = json.load(file)
    test_list = test_dict["data"]


@pytest.mark.parametrize("test_data_item",test_list)
def test_purchaseFlow(browserInstance,test_data_item):

    driver = browserInstance

    loginLogout = loginPage(driver)

    #Part 1 – Pre-Login Setup
    loginLogout.verify_homepage_title_and_URL()

    #Part 2 – Login
    loginLogout.login(test_data_item["username"],test_data_item["password"])

    #productpage will receive the instance of ProductPage class
    ProductPage = loginLogout.validateLogin() #Verify Logged in as username is displayed.


    ProductPage.SearchAndViewProduct()


    loginLogout.logout()
