from Pages.RegistrationPage import SignUpPage
from Pages.BasePage import BasePage


class SignUpWithPhoneNumber(BasePage):
    def test_Sign_Up(self):
        signup = SignUpPage(self.driver)
        signup.click_on_signup_btn()
        signup.register_btn()
        signup.phone_number("01713086265")
        signup.drag_and_drop()
        signup.password_input("abc123")
        signup.birth_month_box()
        signup.birth_month()
        signup.birth_day_box()
        signup.birth_day()
        signup.birth_year_box()
        signup.birth_year()
        signup.gender_box()
        signup.gender()
        signup.full_name("Arfan Abir")
        signup.check_box()
        signup.submit_btn()

