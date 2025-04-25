from selenium.webdriver.common.by import By
from Pages.base_page import Page

class MainPage(Page):
    CONT_BTN = (By.XPATH, "//a[@wized='loginButton']")
    MARKET_BTN = (By.XPATH, "//a[@href='/market-companies']")

    def open_main_page(self):
        self.open_url('https://soft.reelly.io/')

    def log_in(self):
        self.click(*self.CONT_BTN)

    def open_market(self):
        self.click(*self.MARKET_BTN)

#    def place_here(self):
#        self.click(*self.)