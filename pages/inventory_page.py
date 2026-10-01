from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    CART_LINK = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    def title(self):
        return self.text_of(self.PAGE_TITLE)

    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD_BUTTON)

    def cart_count(self):
        return self.text_of(self.CART_BADGE)

    def open_cart(self):
        self.click(self.CART_LINK)