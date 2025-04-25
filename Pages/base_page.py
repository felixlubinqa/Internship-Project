from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, \
            print(f'Expected text did not match actual_text')

    def wait_for_element_visible(self, *locator):
        return self.wait.until(ec.visibility_of_element_located(locator), message=f'Element by {locator} not visible')

    def wait_and_click(self, *locator):
        self.wait.until(ec.element_to_be_clickable(locator), message=f'Element by {locator} not clickable').click()