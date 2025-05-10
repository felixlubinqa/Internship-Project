from Pages.base_page import Page
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class MarketPage(Page):
    HDR_TEXT = (By.XPATH, "//div[@class='market-search-button-block']")
#   DEV_TEXT = (By.XPATH, "//div[text()='Developers']")
    LIC_BANNER = (By.XPATH, "//div[@class='license-block']")

    def check_market_page(self):
        def check_market_page(self):
            market_el = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.HDR_TEXT)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", market_el)
            actual_text = market_el.text
            assert 'Market' in actual_text, f'Error, Market Page not found. Found: {actual_text}'

    def developer_filter(self):
        sleep(3)
        developer_tab = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//div[@wized='marketTagDevelopers']")))
        sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", developer_tab)
        developer_tab.click()
        print(self.driver.page_source)

    #       self.find_element(*self.DEV_TEXT) #For Web
    #       self.click(*self.DEV_TEXT)

    def license_tag(self):
        actual_text = self.find_element(*self.LIC_BANNER).text
        assert 'License' in actual_text, f'Error, Banners not found on page'
#       old locator = self.find_elements(*self.LIC_BANNER)


#//div[@wized='marketTagDevelopers']