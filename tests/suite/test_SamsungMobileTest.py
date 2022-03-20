from Pages.SearchPage import SearchPage
from Pages.BasePage import BasePage


class SamsungSearch(BasePage):
    def test_samsung_mobile_search(self):
        search = SearchPage(self.driver)
        search.search_empty("samsung mobile phone")
        search.search_btn()
        search.count_item()
