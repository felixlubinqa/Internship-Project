from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.Application import Application
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    # Google Chrome
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

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

    ### SAFARI ###
    # context.driver = webdriver.Safari()
    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK CONFIG ###
    ## Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'felixlubin_8b3pgO'
    bs_key = '1mE9qLyKq5qQ36voYGB9'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "os": "OS X",
        "osVersion": "Sonoma",
        'browserName': 'chrome',
        'sessionName': scenario_name,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

#--------------------------------------------------------------

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)


#--------------------------------------------------------------

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()


