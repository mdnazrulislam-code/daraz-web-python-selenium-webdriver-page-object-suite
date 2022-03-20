from Pages.SearchPage import SearchPage
from Pages.BasePage import BasePage


class LaptopSearch(BasePage):
    def test_lenovo_search(self):
        search = SearchPage(self.driver)
        search.search_empty("laptop")
        search.search_btn()
        search.lenovo_laptop()


