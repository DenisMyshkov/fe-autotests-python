from executor.executor import Executor
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SearchPage(Executor):
    search_input = (By.XPATH, '//input')
    category_suggest = (By.XPATH, '//*[contains(text(), "Фрукты")]')
    search_history_item = (By.XPATH, '//*[contains(text(), "брокколи")]')
    search_store_item = (By.XPATH, '//*[contains(text(), "Самокат")]')
    search_store_category_name = (By.XPATH, '//*[contains(text(), "брокколи")]')
    search_results = (By.XPATH, '//*[@qa-locator-name="qa-itemList-item-itemName"]')
    suggests = (By.XPATH, '//*[@qa-locator-name="qa-search-suggests"]')

    def has_suggests_block(self):
        return self.has_node(SearchPage.suggests)

    def open_search_input(self):
        self.find_element(SearchPage.search_input).click()

    def use_placeholder(self):
        element = self.find_element(SearchPage.search_input)
        element.click()
        element.send_keys(Keys.RETURN)


