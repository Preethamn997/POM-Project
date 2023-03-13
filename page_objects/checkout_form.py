from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from page_objects import form_data


# Defining a class CheckForm which extends the BasePage class
class CheckForm(BasePage):
    # Defining private class variables for the form elements
    __e_mail = (By.XPATH, "//input[@id='email']")
    __card_num = (By.XPATH, "//input[@id='card_number']")
    __expiry_date = (By.XPATH, "//input[@id='cc-exp']")
    __ccv_no = (By.XPATH, "//input[@id='cc-csc']")
    __zipcode = (By.XPATH, "//input[@id='billing-zip']")
    __payment_button = (By.XPATH, "//button[@id='submitButton']")

    # Defining a method to fill the form
    def fill_form(self):
        # Filling in the email field
        super()._type(self.__e_mail, form_data.user_e_mail)

        # Filling in the card number field, one digit at a time
        for data in form_data.card_number:
            super()._type(self.__card_num, data)

        # Filling in the expiry date field, one part at a time
        for date in form_data.card_expiry:
            super()._type(self.__expiry_date, date)

        # Filling in the CCV field
        super()._type(self.__ccv_no, form_data.c_c_v)

        # Filling in the ZIP code field
        super()._type(self.__zipcode, form_data.zcode)

    # Defining a method to click the Pay button
    def click_pay(self):
        super()._click(self.__payment_button)
