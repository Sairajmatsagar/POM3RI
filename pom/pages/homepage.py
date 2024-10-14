from selenium.webdriver.common.by import By

from pom.pages.basepage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver
        self.menubarbutton=(By.CLASS_NAME,'bm-burger-button')
        self.logountlink=(By.LINK_TEXT,'Logout')

    def logout(self):
        self.click(self.menubarbutton)
        self.click(self.logountlink)

