from Pages.EnglishToBanglaPage import LanguagePage
from Pages.BasePage import BasePage


class EnglishToBangla(BasePage):
    def test_change_language(self):
        language = LanguagePage(self.driver)
        language.click_language()
        language.click_bangla()
