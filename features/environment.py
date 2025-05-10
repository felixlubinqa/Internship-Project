from app.Application import Application
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
# from allure_behave import
from selenium.webdriver.support.ui import WebDriverWait
# Commands for Allure
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/<>feature

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    # Google Chrome
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    ##Mobile##
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
    #                           desired_capabilities=chrome_options.to_capabilities())

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
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'felixlubin_8b3pgO'
    # bs_key = '1mE9qLyKq5qQ36voYGB9'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "OS X",
    #     "osVersion": "Sonoma",
    #     'browserName': 'chrome',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    ### BROWSERSTACK Mobile CONFIG ###
    bs_user = 'felixlubin_8b3pgO'
    bs_key = '1mE9qLyKq5qQ36voYGB9'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = webdriver.ChromeOptions()

    bstack_options = {
        "osVersion": "13.0",
        "deviceName": "Google Pixel 7",
        "realMobile": "true",
        "local": "false",
        "userName": bs_user,
        "accessKey": bs_key,
        "sessionName": scenario_name
    }

    options.set_capability('bstack:options', bstack_options)
    options.set_capability("browserName", "chrome")
    context.driver = webdriver.Remote(command_executor=url, options=options)
#--------------------------------------------------------------

    #context.driver.maximize_window()
    context.driver.implicitly_wait(3)
    context.driver.wait = WebDriverWait(context.driver, timeout=15)
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


