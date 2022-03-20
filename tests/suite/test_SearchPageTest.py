from Pages.SearchPage import SearchPage
from Pages.BasePage import BasePage


class EmptySearch(BasePage):
    def test_search(self):
        search = SearchPage(self.driver)
        search.search_empty("")
        search.search_btn()
