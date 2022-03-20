import time
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from testconf.run_configuration import headless, linux


class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        # cls.driver.maximize_window()
        options = Options()
        desired_capabilities = DesiredCapabilities.CHROME
        # desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
        desired_capabilities['goog:loggingPrefs'] = {'browser': 'ALL'}
        if headless:
            options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        if linux:
            cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options,
                                           desired_capabilities=desired_capabilities)
        else:
            cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options,
                                           desired_capabilities=desired_capabilities)
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(3000)
        cls.driver.get("https://www.daraz.com.bd/")
        print("Test Started")

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()
        print("Test Complete")