import time

import pytest
from selenium import webdriver

import logging

def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser name: chrome or firefox")

@pytest.fixture
def browserInstance(request):
    global driver
    chromeOption = webdriver.ChromeOptions()
    chromeOption.add_argument("--incognito")
    chromeOption.add_argument("--start-maximized")

    edgeOption = webdriver.EdgeOptions()
    edgeOption.add_argument("--incognito")
    edgeOption.add_argument("--start-maximized")


    browerName = request.config.getoption("browser_name")   #get value from command line argument

    if browerName == "chrome":
        driver = webdriver.Chrome(options=chromeOption)
    if browerName == "edge":
        driver = webdriver.Edge(options=edgeOption)

    driver.get("https://automationexercise.com/")
    time.sleep(1)
    driver.implicitly_wait(4)
    yield driver
    driver.close()