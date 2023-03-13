from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


# Defining a class PaymentPage which extends the BasePage class
class PaymentPage(BasePage):
    __pay_with_card_btn = (By.XPATH, "//*[contains(text(),'Pay with Card')]")
    __payment_form = (By.XPATH, "//iframe[@name='stripe_checkout_app']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # click on pay with card button
    def click_pay_with_card(self):
        super()._click(self.__pay_with_card_btn)

    # switch to payment form iframe
    def switch_payment_form(self):
        super()._switch_frame(self.__payment_form)

    # switch back to main window from iframe
    def switch_to_payment_status(self):
        super()._switch_to_window_from_frame()
