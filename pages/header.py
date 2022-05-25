from executor.executor import Executor
from selenium.webdriver.common.by import By


class Header(Executor):
    user_info = (By.XPATH, '//*[@qa-locator-name="qa-header-menuButton"]')
    not_correct_user_info = (By.XPATH, '//*[@qa-locato-name="qa-header-menuButton"]')

    def open_incorrect_user_info(self):
        self.wait_until_element_to_be_clickable(Header.not_correct_user_info)
        element = self.find_element(Header.not_correct_user_info)
        element.click()

    def open_user_info(self):
        self.click(Header.user_info)
