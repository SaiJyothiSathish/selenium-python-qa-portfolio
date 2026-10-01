from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
def test_valid_user_can_log_in(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url
@pytest.mark.regression
def test_invalid_user_sees_error_message(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("wrong_user", "wrong_password")

    assert "Username and password do not match" in login_page.error_message()