

from Locators.locators import English2Bangla
from Pages.HomePage import HomePage


class LanguagePage(HomePage):
    def __init__(self, driver):
        self.locator = English2Bangla
        self.driver = driver
        super(LanguagePage, self).__init__(driver)

    def click_language(self):
        self.find_element(*self.locator.LANGUAGE).click()

    def click_bangla(self):
        self.find_element(*self.locator.BANGLA).click()
