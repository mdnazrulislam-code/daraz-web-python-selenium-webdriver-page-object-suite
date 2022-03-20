from Pages.SearchPage import SearchPage
from Pages.BasePage import BasePage


class ListView(BasePage):
    def test_gaming_laptop(self):
        search = SearchPage(self.driver)
        search.search_empty("laptop")
        search.search_btn()
        search.gaming()

