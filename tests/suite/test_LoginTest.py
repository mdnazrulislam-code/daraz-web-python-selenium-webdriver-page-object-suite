from Pages.LoginPage import LoginPage
from Pages.BasePage import BasePage


class LoginTest(BasePage):
    def test_login_page(self):
        loginPage=LoginPage(self.driver)
        loginPage.click_on_login()
        loginPage.set_email("01713086265")
        loginPage.set_password("abc123")
        loginPage.click_sign_in()
