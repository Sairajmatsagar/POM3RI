import time


class TestLogin:

    def test_login(self,setup_and_teardown):
        self.loginpage.login('standard_user','secret_sauce')
        time.sleep(5)