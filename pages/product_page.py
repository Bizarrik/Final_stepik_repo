from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_add_item_to_basket(self):
        self.should_be_add_to_basket_button()
        self.should_click_button_and_add_item_to_basket()
        self.should_solve_quiz()
        self.should_be_success_message_with_item_name()
        self.should_be_info_message_with_item_price()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not present"
        assert True

    def should_click_button_and_add_item_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_solve_quiz(self):
        self.solve_quiz_and_get_code()

    def should_be_success_message_with_item_name(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "There is no success message"
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_name_in_message = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_MESSAGE).text
        assert item_name_in_message == item_name, f"Item name in success message is '{item_name_in_message}', should be '{item_name}'"
        # assert f"{item_name} has been added to your basket." in self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text, "Success message is not correct"

    def should_be_info_message_with_item_price(self):
        assert self.is_element_present(*ProductPageLocators.INFO_MESSAGE), "There is no info message"
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert item_price in self.browser.find_element(*ProductPageLocators.INFO_MESSAGE).text, "The item price in info message differs from item price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but it should"