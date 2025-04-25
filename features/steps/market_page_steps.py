from time import sleep
from behave import When, Then
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as ec
#from time import sleep

@When ('Click on Developers filter at the top of the page')
def developer_filter(context):
    context.app.market_page.developer_filter()
    sleep(4)

@Then ('Verify all cards have the license tag')
def license_tag(context):
    context.app.market_page.license_tag()