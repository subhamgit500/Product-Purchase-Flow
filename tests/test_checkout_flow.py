import json

import pytest

from pageObjects.login_logout import loginPage

with open("C:\\PythonProject\\ProductPurchaseFlow\\utilities\\test_data.json") as file:
    test_dict = json.load(file)
    test_list = test_dict["data"]


@pytest.mark.parametrize("test_data_item",test_list)
def test_purchaseFlow(browserInstance,test_data_item):

    driver = browserInstance

    loginLogout = loginPage(driver)
    loginLogout.verify_homepage_title_and_URL()
    loginLogout.login(test_data_item["username"],test_data_item["password"])
    loginLogout.validateLogin()

    loginLogout.logout()