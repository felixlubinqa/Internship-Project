from Pages.base_page import Page
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as ec
#from time import sleep

class MarketPage(Page):
    HDR_TEXT = (By.XPATH, "//div[@class='proparties_text_block mobile']")
    DEV_TEXT = (By.XPATH, "//div[@class='tag-text-proparties']")
    LIC_BANNER = (By.XPATH, "//div[@class='license-block']")

    def check_market_page(self):
        actual_text = self.find_element(*self.HDR_TEXT).text
        assert 'Market' in actual_text, f'Error, Market Page not found'
#       old locator = self.find_element(*self.HDR_TEXT)

    def developer_filter(self):
        self.find_element(*self.DEV_TEXT)

    def license_tag(self):
        actual_text = self.find_element(*self.LIC_BANNER).text
        assert 'License' in actual_text, f'Error, Banners not found on page'
#       old locator = self.find_elements(*self.LIC_BANNER)


#//div[@wized='marketTagDevelopers']