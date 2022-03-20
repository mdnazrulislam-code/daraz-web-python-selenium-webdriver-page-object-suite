from Pages.SearchPage import SearchPage
from Pages.BasePage import BasePage


class SamsungSearch(BasePage):
    def test_samsung_search(self):
        search = SearchPage(self.driver)
        search.search_empty("samsung")
        search.search_btn()
