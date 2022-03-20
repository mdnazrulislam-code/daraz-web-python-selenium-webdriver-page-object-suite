from Pages.SearchPage import SearchPage
from Pages.BasePage import BasePage


class LaptopSearch(BasePage):
    def test_walton_search(self):
        search = SearchPage(self.driver)
        search.search_empty("laptop")
        search.search_btn()
        search.view_more()
        search.walton_laptop()


