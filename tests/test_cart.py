from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
def test_user_can_add_backpack_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    assert inventory_page.title() == "Products"

    inventory_page.add_backpack_to_cart()

    assert inventory_page.cart_count() == "1"