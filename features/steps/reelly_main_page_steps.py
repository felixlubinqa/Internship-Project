from os import waitpid
from time import sleep
from behave import Given, When, Then


@Given ('Open the main page')
def open_home_page(context):
    context.app.reelly_main_page.open_home_page()
    sleep(4)

@When ("Enter username")
def username_entry(context):
    context.app.reelly_main_page.username_entry()

@When ("Type password")
def password_entry(context):
    context.app.reelly_main_page.password_entry()
#    sleep(3)

@When ("Log in to the page")
def log_in(context):
    context.app.reelly_main_page.log_in()
    sleep(3)

@When ("Click on 'market' on the left side menu")
def open_market(context):
    context.app.reelly_main_page.open_market()

@Then ('Verify the right page opens')
def check_market_page(context):
    context.app.market_page.check_market_page()
