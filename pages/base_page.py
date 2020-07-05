#Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать:
from selenium.common.exceptions import NoSuchElementException


class BasePage():
    # добавим конструктор — метод, который вызывается, когда мы создаем объект.
    def __init__(self, browser, url):
        #в качестве параметров мы передаем экземпляр драйвера и url адрес.
        self.browser = browser
        self.url = url

    def open(self):
        #Он должен открывать нужную страницу в браузере, используя метод get()
        self.browser.get(self.url)
    #Добавим команду для неявного ожидания со значением по умолчанию в 10
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    #Рализуем метод, в котором будем перехватывать исключение.
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
#Отлично! Теперь для всех проверок, что элемент действительно присутствует на странице, мы можем использовать этот метод.