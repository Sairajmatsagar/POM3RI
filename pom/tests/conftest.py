import pytest
from selenium import webdriver

from pom.pages.homepage import HomePage
from pom.pages.loginpage import LoginPage





@pytest.fixture()
def setup_and_teardown(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.saucedemo.com/v1/index.html')
    request.cls.loginpage = LoginPage(driver)
    request.cls.homepage = HomePage(driver)
    request.cls.driver = driver
    yield
    driver.close()
