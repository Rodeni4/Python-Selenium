from .base_page import BasePage

#импортируйте новый класс с локаторами
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
    #модифицируем метод проверки ссылки на логин так, чтобы он выдавал адекватное сообщение об ошибке:
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
