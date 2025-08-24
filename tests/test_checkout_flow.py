import json, os

import pytest

import logging

from pageObjects.login_logout import LoginPage


#Retrive test data
# Better: use os.path or pathlib so test runs on any machine:
file_path = os.path.join(os.path.dirname(__file__), "../utilities/test_data.json")
with open(file_path, "r") as file:
    test_dict = json.load(file)
    test_list = test_dict["data"]



logger = logging.getLogger(__name__)  #for logging messages in console or run result.

@pytest.mark.parametrize("test_data_item",test_list,ids=[f"User:{item['username']}" for item in test_list])
def test_purchaseFlow(browserInstance,test_data_item):

    driver = browserInstance
    login_logout = LoginPage(driver)

    #Part 1 – Pre-Login Setup
    logger.info("\nStep 1: Verify Homepage\n")
    login_logout.verify_homepage_title_and_URL()

    #Part 2 – Login
    logger.info("\nStep 2: Perform Login\n")
    login_logout.login(test_data_item["username"],test_data_item["password"])

    logger.info("\nStep 3: Verify Login\n")
    # product_page will receive the instance of ProductPage class from login_logout.validateLogin method
    login_logout.validate_login()  # Verify Logged in as username is displayed.

    #Part 3 – Product Browsing
    logger.info("\nStep 4: Select Product\n")
    product_page = login_logout.go_to_product_page()
    product_page.search_and_view_product(test_data_item["product_to_search"],test_data_item["category"],test_data_item["product_category"])

    # Part 7 – Logout
    logger.info("\nStep 5: Perform Logout\n")
    login_logout.logout()
