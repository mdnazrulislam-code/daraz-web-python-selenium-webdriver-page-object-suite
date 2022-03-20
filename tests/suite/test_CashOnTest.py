from Pages.SearchPage import SearchPage
from Pages.BasePage import BasePage


class LaptopSearch(BasePage):
    def test_cash_on_Delivery(self):
        search = SearchPage(self.driver)
        search.search_empty("laptop")
        search.search_btn()
        search.scroll_down()
        search.cash_on_delivery()


