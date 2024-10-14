import time


class TestLogout:
    def test_logout(self,setup_and_teardown):
        self.loginpage.login('standard_user', 'secret_sauce')
        time.sleep(3)
        self.homepage.logout()
        time.sleep(3)
