from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_page_url()
        self.go_to_product_page()
        self.solve_quiz_and_get_code()
        self.should_message_added_basket()
        self.should_message_product_cost()
        self.should_not_be_success_message()

    def should_be_product_page_url(self):
        # реализуйте проверку на корректный url адрес
        assert "?promo=offer" in self.browser.current_url, "'?promo=newYear' not in current url"

    def go_to_product_page(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_message_added_basket(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADDED_BASKET)
        #assert "has been added to your basket" in message.text, "No message 'has been added to your basket'"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text == message.text, "Product name does not match"

    def should_message_product_cost(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_COST_BASKET)
        assert "Your basket total is now" in message.text, "No message 'Your basket total is now'"
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST)
        assert product_cost.text in message.text, "Basket price doesn't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"





