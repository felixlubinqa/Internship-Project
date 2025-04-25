from selenium.webdriver.common.by import By
from Pages.base_page import Page

class SidePage(Page):
    SIGN_IN_SIDE = (By.XPATH, "//button[@data-test='accountNav-signIn']")
    SIDE_CART_ADD = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
    CART_ITEM_ADDED = (By.XPATH, "//span[contains(text(), 'Added to cart')]")
    VIEW_CART_SIDE = (By.CSS_SELECTOR, "[href='/cart']")


    def sign_in_side(self):
        self.click(*self.SIGN_IN_SIDE)

    def add_to_cart_side(self):
        self.wait_and_click(*self.SIDE_CART_ADD)

    def item_added_side(self):
        self.wait_for_element_visible(*self.CART_ITEM_ADDED)

    def view_cart_side_page(self):
        self.wait_and_click(*self.VIEW_CART_SIDE)


