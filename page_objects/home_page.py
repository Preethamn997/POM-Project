from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage
from page_objects.form_data import url_weather_shopper


class HomePage(BasePage):
    # Define class variables for the web elements
    __buy_moisture_btn = (By.XPATH, "//button[text()='Buy moisturizers']")
    __buy_sunscreen_btn = (By.XPATH, "//button[text()='Buy sunscreens']")
    __add_button = (By.XPATH, "//button[contains(text(),'Add')]")
    __item_price = (By.XPATH, "//div[@class='container']//div//p[2]")
    __temperature = (By.XPATH, "//span[@id='temperature']")

    def __init__(self, driver: WebDriver):
        # Call the constructor of the base class and pass the driver instance
        super().__init__(driver)

    def open(self):
        # Call the _open_url method of the base class and pass the URL of the page
        super()._open_url(url_weather_shopper)

    def read_temperature(self, ):
        # Call the _get_text method of the base class to get the text of the temperature web element
        temperature = super()._get_text(self.__temperature)
        # Parse the temperature text and convert it to an integer
        current_temperature = int(temperature.strip().split()[0])
        # Print the current temperature for debugging purposes
        print(current_temperature)
        # Return the current temperature as an integer
        return current_temperature

    def select_moisturizer(self):
        # Call the _click method of the base class to click the Buy moisturizers button
        super()._click(self.__buy_moisture_btn)

    def select_sunscreen(self):
        # Call the _click method of the base class to click the Buy sunscreens button
        super()._click(self.__buy_sunscreen_btn)

    def current_page_title(self):
        # Return the title of the current page using the _title method of the base class
        return super()._title
