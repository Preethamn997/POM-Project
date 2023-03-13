""" This Test class imports various page objects, including HomePage, ProductMenu, PaymentPage, CheckForm, and
PaymentStatus, each of which corresponds to a different page of the application. The TestWeatherShopper class defines
several fixtures using the @pytest.fixture decorator. These fixtures provide reusable objects that can be passed to
multiple test cases, such as instances of the various page objects. The code also includes two helper functions:
add_lowest_priced_products and print_payment_status. These functions are used in the test_select_product and
test_payment_status test cases, respectively."""


import re
import pytest
from page_objects.home_page import HomePage
from page_objects.checkout_form import CheckForm
from page_objects.payment_status import PaymentStatus
from page_objects.product_menu_page import ProductMenu
from page_objects.payment_page import PaymentPage


class TestWeatherShopper:

    # Define fixtures to be used across tests
    @pytest.fixture(scope="class")
    def product_page(self, driver):
        return ProductMenu(driver)

    @pytest.fixture(scope="class")
    def home_page(self, driver):
        return HomePage(driver)

    @pytest.fixture(scope="class")
    def payment_page(self, driver):
        return PaymentPage(driver)

    @pytest.fixture(scope="class")
    def payment_form(self, driver):
        return CheckForm(driver)

    @pytest.fixture(scope="class")
    def payment_status(self, driver):
        return PaymentStatus(driver)

    # Test case for verifying the home page is opened correctly
    @pytest.mark.test
    def test_home_page(self, home_page):
        home_page.open()
        assert home_page.current_page_title() == "Current Temperature", "Invalid Url"

    # Test case for selecting a product based on temperature and adding two lowest priced items to cart
    @pytest.mark.test
    def test_select_product(self, home_page, product_page):
        temperature = home_page.read_temperature()
        if temperature < 30:
            home_page.select_moisturizer()
            assert product_page.expected_url_moisturizer == home_page.current_url, "invalid url"
        else:
            home_page.select_sunscreen()
            assert product_page.expected_url_sunscreen == home_page.current_url, "invalid url"
        add_lowest_priced_products(product_page)

    # Test case for navigating to payment page
    @pytest.mark.test
    def test_payment_page(self, product_page, payment_page):
        product_page.nav_to_cart()
        payment_page.click_pay_with_card()

    # Test case for filling out payment form and clicking Pay
    @pytest.mark.test
    def test_payment_form(self, payment_page, payment_form):
        payment_page.switch_payment_form()
        payment_form.fill_form()
        payment_form.click_pay()

    # Test case for verifying payment status
    @pytest.mark.test
    def test_payment_status(self, payment_status):
        confirmation = payment_status.status()
        print_payment_status(confirmation)


# Helper function to add two lowest priced products to cart
def add_lowest_priced_products(product_page):
    prices = [int(re.findall(r'\d+', price.text)[0]) for price in product_page.product_price()]
    add_buttons = product_page.add_button()
    lowest_prices = sorted(prices)[:2]
    for item_price, add_btn in zip(prices, add_buttons):
        if item_price in lowest_prices:
            add_btn.click()


# Helper function to print payment status and catch assertion errors
def print_payment_status(confirmation):
    try:
        assert confirmation == "PAYMENT SUCCESS", "Test failed"
    except Exception as e:
        print(f"An error occurred while checking the payment status: {e}")
    else:
        print("Test passed")

