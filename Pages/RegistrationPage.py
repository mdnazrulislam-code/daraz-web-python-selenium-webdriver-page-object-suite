import time

from selenium.webdriver import ActionChains

from Locators.locators import RegistrationPage
from Pages.HomePage import HomePage


class SignUpPage(HomePage):
    def __init__(self, driver):
        self.locator = RegistrationPage
        self.driver = driver
        super(SignUpPage, self).__init__(driver)

    def click_on_signup_btn(self):
        self.find_element(*self.locator.SIGN_BTN).click()

    def register_btn(self):
        self.find_element(*self.locator.REGISTER).click()

    def signup_email(self):
        self.find_element(*self.locator.SIGNUP_EMAIL).click()

    def phone_number(self, phone_number):
        self.find_element(*self.locator.PHONE_NUMBER).send_keys(phone_number)

    def drag_and_drop(self):
        start = self.find_element(*self.locator.DRAG_DROP_START)
        stop = self.find_element(*self.locator.DRAG_DROP_STOP)
        action = ActionChains(self.driver)
        action.click_and_hold(start).move_to_element(stop).pause(2).move_by_offset(340, 0).release().perform()
        print("Dragging & dropping test case successful\n")
        time.sleep(5)

    def password_input(self, password):
        self.find_element(*self.locator.PASSWORD_INPUT).send_keys(password)

    def birth_month_box(self):
        self.find_element(*self.locator.B_MONTH_BOX).click()
        time.sleep(2)

    def birth_month(self):
        self.find_element(*self.locator.BIRTH_MONTH).click()
        time.sleep(2)

    def birth_day_box(self):
        self.find_element(*self.locator.B_DAY_BOX).click()
        time.sleep(2)

    def birth_day(self):
        self.find_element(*self.locator.B_DAY).click()
        time.sleep(2)

    def birth_year_box(self):
        self.find_element(*self.locator.B_YEAR_BOX).click()
        time.sleep(2)

    def birth_year(self):
        self.find_element(*self.locator.B_YEAR).click()
        time.sleep(2)

    def gender_box(self):
        self.find_element(*self.locator.GENDER_BOX).click()
        time.sleep(2)

    def gender(self):
        self.find_element(*self.locator.GENDER).click()
        time.sleep(2)

    def full_name(self, name):
        self.find_element(*self.locator.FULL_NAME).send_keys(name)

    def check_box(self):
        self.find_element(*self.locator.CHECK_BOX).click()

    def submit_btn(self):
        self.find_element(*self.locator.SIGN_UP).click()