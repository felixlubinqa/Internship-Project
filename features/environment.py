from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.firefox.webdriver import WebDriver
#from webdriver_manager.firefox import GeckoDriverManager
#from selenium.webdriver.chromium.options import ChromiumOptions
from app.Application import Application
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def browser_init(context):
    """
    :param context: Behave context
    """

# Google Chrome
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)


# Headless
#    driver_path = ChromeDriverManager().install()
#    service = Service(driver_path='./chromedriver.exe')
#    options = webdriver.ChromeOptions()
#    options.binary_location = '/usr/bin/google-chrome-unstable'
#    options.add_argument('headless')
#    context.driver = webdriver.ChromeOptions(chrome_options=options)


# Firefox
#   driver_path = GeckoDriverManager().install()
#   service = Service(driver_path)
#   context.driver = webdriver.Firefox(service=service)
#    options = get_default_chrome_options()
#    driver = webdriver.Remote(command_executor=server, options=options)



#--------------------------------------------------------------

#    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)

#--------------------------------------------------------------

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
