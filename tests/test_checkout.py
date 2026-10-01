from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
def test_customer_can_complete_checkout(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()

    assert inventory_page.cart_count() == "1"

    inventory_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_customer_details("Sai", "Kumar", "600001")
    assert checkout_page.page_title() == "Checkout: Overview"
    checkout_page.finish_order()

    assert checkout_page.completion_message() == "Thank you for your order!"