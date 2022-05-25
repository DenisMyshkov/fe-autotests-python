from executor.executor import Executor
from selenium.webdriver.common.by import By


class UserInfo(Executor):
    cart = (By.XPATH, '//*[@qa-locator-name="qa-menu-cart"]')
    orders = (By.XPATH, '//*[@qa-locator-name="qa-menu-order"]')

    def open_cart(self):
        self.wait_until_element_to_be_clickable(UserInfo.cart)
        self.click(UserInfo.cart)

    def open_order_list(self):
        self.wait_until_element_to_be_clickable(UserInfo.orders)
        self.click(UserInfo.orders)
