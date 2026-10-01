from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "[data-test='complete-header']")
    PAGE_TITLE = (By.CSS_SELECTOR, "[data-test='title']")

    def enter_customer_details(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_order(self):
        self.click(self.FINISH_BUTTON)

    def completion_message(self):
        return self.text_of(self.COMPLETE_HEADER)

    def page_title(self):
        return self.text_of(self.PAGE_TITLE)