from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Common actions used by all page objects."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(text)

    def text_of(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text