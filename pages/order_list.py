from executor.executor import Executor
from selenium.webdriver.common.by import By


class OrderList(Executor):
    order_total_sum = (By.XPATH, '//*[@qa-locator-name="qa-order-orderTotalAmount"]')
    order_status = (By.XPATH, '//*[@qa-locator-name="qa-order-orderStatus"]')
    cancel_order_button = (By.XPATH, '//*[@qa-locator-name="qa-order-cancelOrder"]')
    cancel_order_submit_button = (By.XPATH, '//*[@qa-locator-name="qa-bottomSlider-cancelOrder"]')
    understand_button = (By.XPATH, '//*[@qa-locator-name="qa-bottomSlider-understand"]')
    order_number = (By.XPATH, '//*[@qa-locator-name="qa-order-orderNumber"]')
    order = (By.XPATH, '//*[@qa-locator-id="qa-order-"]')
    cancel_order_locator = "//*[@qa-locator-name='qa-order-cancelOrder']"
    home_button = (By.XPATH, '/html/body/div/div/div[1]/div/div/header/a')

    def cancel_current_order(self, order_number):
        current_order = (By.XPATH, OrderList.order[1][:29]+order_number+OrderList.order[1][29:])
        self.click(current_order)
        self.click(OrderList.cancel_order_button)
        self.click(OrderList.cancel_order_submit_button)
        self.click(OrderList.understand_button)

    def get_order_status(self, order_number):
        current_order = (By.XPATH, OrderList.order[1][:29]+order_number+OrderList.order[1][29:])
        return self.driver.find_element(*current_order).find_element(*OrderList.order_status).text

    def get_order_sum_by_number(self, order_number):
        current_order = (By.XPATH, OrderList.order[1][:29]+order_number+OrderList.order[1][29:])
        return self.driver.find_element(*current_order).find_element(*OrderList.order_total_sum).text

    def tap_home_button(self):
        self.click(OrderList.home_button)
