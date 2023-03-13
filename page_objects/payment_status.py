from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


# Defining a class PaymentStatus which extends the BasePage class
class PaymentStatus(BasePage):
    # Defining private class variables for the payment status element
    __check_payment_status = (By.XPATH, "//*[@class='row justify-content-center']//h2")

    # Define a method to get text of payment confirmation
    def status(self):
        return super()._get_text(self.__check_payment_status)

    # Define a method to switch payment frame to default window
    def switch_to_status_page(self):
        super()._switch_to_window_from_frame()
