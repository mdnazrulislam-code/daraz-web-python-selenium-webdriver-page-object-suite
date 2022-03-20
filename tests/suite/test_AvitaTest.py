from Pages.SearchPage import SearchPage
from Pages.BasePage import BasePage


class LaptopSearch(BasePage):
    def test_avita_search(self):
        search = SearchPage(self.driver)
        search.search_empty("laptop")
        search.search_btn()
        search.avita_laptop()


