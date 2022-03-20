from Pages.SearchPage import SearchPage
from Pages.BasePage import BasePage


class LaptopSearch(BasePage):
    def test_laptop_search(self):
        search = SearchPage(self.driver)
        search.search_empty("laptop")
        search.search_btn()
