from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Pages.base_page import Page


class MainPage(Page):
    CONT_BTN = (By.XPATH, "//a[@wized='loginButton']")
    MARKET_BTN = (By.XPATH, "//div[@wized='mobileMenuForVerifiedUsers']//a[@href='/calendar']")
    MARKET_BTN2 = (By.XPATH, "//a[@href='/market-companies']")
    PASS_WORD = (By.NAME, 'Password')
    USER_NAME = (By.NAME, 'email-2')

    def open_home_page(self):
        self.open_url('https://soft.reelly.io/')

    def log_in(self):
        self.click(*self.CONT_BTN)

    # def open_market(self):
    #     self.click(*self.MARKET_BTN) #.until(EC.element_to_be_clickable)

    def open_market(self):
        def open_market(self):
            market_el = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.MARKET_BTN)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", market_el)  # Scrolls the element into view
            market_el.click()  # Now click the element
            sleep(3)
            self.click(*self.MARKET_BTN2)

    def username_entry(self):
        self.input_text('felix.lubin.qa@gmail.com', *self.USER_NAME)

    def password_entry(self):
        self.input_text('OldrocktoQA25', *self.PASS_WORD)

#send_keys('OldrocktoQA25')
