from Pages.SearchPage import SearchPage
from Pages.BasePage import BasePage



class LaptopAssert(BasePage):
    def test_laptop_assert(self):
        search = SearchPage(self.driver)
        search.search_empty("laptop")
        search.search_btn()
        search.count_item()


