import time

from Locators.locators import SearchPageLocator
from Pages.HomePage import HomePage


class SearchPage(HomePage):

    def __init__(self, driver):
        self.locator = SearchPageLocator
        self.driver = driver
        super(SearchPage, self).__init__(driver)

    def search_empty(self,input):
        self.find_element(*self.locator.SEARCH_BAR).send_keys(input)

    def search_btn(self):
        self.find_element(*self.locator.SEARCH_BTN).click()

    def count_item(self):
        self.find_element(*self.locator.COUNT_ITEM).text

    def list_view(self):
        self.find_element(*self.locator.LIST_VIEW).click()

    def traditional(self):
        self.find_element(*self.locator.TRADITIONAL).click()

    def gaming(self):
        self.find_element(*self.locator.GAMING_LAPTOP).click()

    def basic(self):
        self.find_element(*self.locator.BASIC).click()

    def asus(self):
        self.find_element(*self.locator.ASUS).click()

    def view_more(self):
        self.find_element(*self.locator.VIEW_MORE).click()

    def walton_laptop(self):
        self.find_element(*self.locator.WALTON_LAPTOP).click()

    def hp_laptop(self):
        self.find_element(*self.locator.HP_LAPTOP).click()

    def lenovo_laptop(self):
        self.find_element(*self.locator.LENOVO_LAPTOP).click()

    def dell_laptop(self):
        self.find_element(*self.locator.DELL_LAPTOP).click()

    def avita_laptop(self):
        self.find_element(*self.locator.AVITA_LAPTOP).click()

    def scroll_down(self):
        self.find_element(*self.locator.LOCATION_SCROLL).click()

    def cash_on_delivery(self):
        self.find_element(*self.locator.CASH_ON_DELIVERY).click()
