
from selenium.webdriver.common.by import By
from Pages.base_page import Page

class MainPage(Page):
    CONT_BTN = (By.XPATH, "//a[@wized='loginButton']")
    MARKET_BTN = (By.XPATH, "//a[@href='/market-companies']")
    PASS_WORD = (By.NAME, 'Password')
    USER_NAME = (By.NAME, 'email-2')
        #(By.XPATH, "//input[@wized='emailInput')")

    def open_home_page(self):
        self.open_url('https://soft.reelly.io/')

    def log_in(self):
        self.click(*self.CONT_BTN)

    def open_market(self):
        self.click(*self.MARKET_BTN)

    def username_entry(self):
        self.input_text('felix.lubin.qa@gmail.com', *self.USER_NAME)

    def password_entry(self):
        self.input_text('OldrocktoQA25', *self.PASS_WORD)

#send_keys('OldrocktoQA25')
