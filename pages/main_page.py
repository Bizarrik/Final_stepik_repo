from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # def should_open_basket_page(self):
    #     basket_button = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
    #     basket_button.click() перенесено в BasePage

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_empty_basket_message(self):
        basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert "Your basket is empty. Continue shopping" in basket_message.text, "Basket is not empty"