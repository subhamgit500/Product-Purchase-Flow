import pytest
from selenium import webdriver

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
    driver.implicitly_wait(4)
    yield driver
    driver.close()