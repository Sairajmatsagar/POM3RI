from selenium.webdriver.common.by import By

from pom.pages.basepage import BasePage
from pom.pages.homepage import HomePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username_textfield = (By.ID, 'user-name')
        self.password_textfeild = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')

    def login(self, username, password):
        # driver.find_element((By.ID,'user-name')).send_keys('username')
        self.send_keys(self.username_textfield, username)
        self.send_keys(self.password_textfeild, password)
        self.click(self.login_button)

