from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_empty_basket_negative(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def should_be_empty_basket_message(self):
        basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        assert "Your basket is empty. Continue shopping" in basket_message.text, "Basket is not empty"