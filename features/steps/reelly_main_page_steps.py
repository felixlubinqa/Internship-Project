from behave import Given, When, Then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

@Given ('Open the main page')
def open_main_page(context):
    context.driver.get('https://soft.reelly.io/')

#    @When ("Log in to the page")
#    def log_in(context):
#
#        @When ("Click on 'market' on the left side menu")
#        def open_market(context):
#
#@Then ('Verify the right page opens')
#def check_market_page(context):
#
#    @When ('Click on Developers filter at the top of the page')
#    def dev_filter(context):
#
#@Then ('Verify all cards have the license tag')
#def open_market(context):