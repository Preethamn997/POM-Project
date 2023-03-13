from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ProductMenu(BasePage):
    _url_moisture = "https://weathershopper.pythonanywhere.com/moisturizer"
    _url_sunscreen = "https://weathershopper.pythonanywhere.com/sunscreen"
    __add_button = (By.XPATH, "//button[contains(text(),'Add')]")
    __item_price = (By.XPATH, "//div[@class='container']//div//p[2]")
    __click_cart = (By.XPATH, "//*[@class= 'thin-text nav-link']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url_moisturizer(self) -> str:
        return self._url_moisture

    @property
    def expected_url_sunscreen(self) -> str:
        return self._url_sunscreen

    def product_price(self):
        return super()._find_all(self.__item_price)

    def add_button(self):
        return super()._find_all(self.__add_button)

    def nav_to_cart(self):
        super()._click(self.__click_cart)
