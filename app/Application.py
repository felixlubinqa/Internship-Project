from Pages.base_page import Page
from Pages.market_page import MarketPage
from Pages.reelly_main_page import MainPage
from Pages.side_bar_page import SidePage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = Page(driver)
        self.reelly_main_page = MainPage(driver)
        self.side_bar_page = SidePage(driver)
        self.market_page = MarketPage(driver)
