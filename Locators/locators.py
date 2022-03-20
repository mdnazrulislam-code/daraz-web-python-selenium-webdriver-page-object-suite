from selenium.webdriver.common.by import By


class SignInPageLocators(object):
    LOGIN_BTN = (By.ID, "anonLogin")
    SET_EMAIL = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[1]/input")
    SET_PASS = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[2]/input")
    CLICK_SIGNIN_BTN = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div[1]/button")


class English2Bangla(object):
    LANGUAGE = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div[1]/div/div[8]/span")
    BANGLA = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div[1]/div/div[8]/div/div/div[1]")


class SearchPageLocator(object):
    SEARCH_BAR = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/form/div/div[1]/input[1]")
    SEARCH_BTN = (By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/form/div/div[2]/button")
    COUNT_ITEM = (By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]")
    LIST_VIEW = (By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/div/div[4]/span[2]/i")
    TRADITIONAL = (By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/div/a[2]")
    GAMING_LAPTOP = (By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/div/a[5]")
    BASIC = (By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div[1]/div/a[1]")
    ASUS = (By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/label[1]/span[2]")
    VIEW_MORE = (By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]")
    WALTON_LAPTOP = (By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/label[10]/span[2]")
    HP_LAPTOP = (By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/label[3]/span[2]")
    LENOVO_LAPTOP = (By.XPATH,"/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/label[2]/span[2]")
    DELL_LAPTOP = (By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/label[7]/span[2]")
    AVITA_LAPTOP = (By.XPATH,"/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/label[6]/span[2]")
    LOCATION_SCROLL = (By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[4]/div[1]")
    CASH_ON_DELIVERY = (By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/div/div/label[2]/span[2]")


class RegistrationPage(object):
    SIGN_BTN = (By.ID, "anonLogin")
    REGISTER = (By.XPATH,"/html/body/div[2]/div/div[2]/div/div[1]/div/span/a")
    PHONE_NUMBER  = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[1]/input")
    DRAG_DROP_START = (By.ID, "nc_2_n1z")
    DRAG_DROP_STOP = (By.ID, "nc_2_wrapper")
    PASSWORD_INPUT = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[3]/input")
    B_MONTH_BOX = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/span/span/span")
    BIRTH_MONTH = (By.XPATH, "/html/body/div[5]/div/div/ul/li[6]")
    B_DAY_BOX = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[4]/div[1]/div[2]/div[2]/span[1]/span/span")
    B_DAY = (By.XPATH, "/html/body/div[5]/div/div/ul/li[26]")
    B_YEAR_BOX = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[4]/div[1]/div[2]/div[2]/span[2]/span/span")
    B_YEAR = (By.XPATH, "/html/body/div[5]/div/div/ul/li[27]")
    GENDER_BOX = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[1]/div[4]/div[2]/div/span/span/span")
    GENDER = (By.XPATH, "/html/body/div[5]/div/div/ul/li[1]")
    FULL_NAME = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div[1]/input")
    CHECK_BOX = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div[2]/label")
    SIGN_UP = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div[3]/button")
    SIGNUP_EMAIL = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/form/div/div[2]/div[5]/div/button")



