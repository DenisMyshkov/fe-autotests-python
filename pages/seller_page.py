from executor.executor import Executor
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException


class SellerPage(Executor):
    seller_name = (By.XPATH, '//*[@qa-locator-name="qa-shopHeader-shopName"]')
    categories = (By.XPATH, '//*[@qa-locator-name="qa-categoryList-category"]')
    all_products = (By.XPATH, '//*[@qa-locator-name="qa-categoryList-allProducts"]')
    items = (By.XPATH, '//*[@qa-locator-name="qa-itemList-item"]')
    item_name = (By.XPATH, '//*[@qa-locator-name="qa-itemList-item-itemName"]')
    add_item_to_cart_button = (By.TAG_NAME, 'button')
    add_item_button = (By.XPATH, '//*[@qa-locator-name="qa-itemList-item-addItem"]')
    search_input = (By.ID, 'search-input')
    search_input_second = (By.XPATH, '//input')
    no_button = (By.XPATH, '//*[@qa-locator-name="qa-bottomSlider-isAdult-noButton"]')
    yes_button = (By.XPATH, '//*[@qa-locator-name="qa-bottomSlider-isAdult-yesButton"]')

    def open_category_by_name(self, category_name):
        self.click((By.PARTIAL_LINK_TEXT, category_name))

    def open_all_products(self):
        self.click(SellerPage.all_products)

    def add_first_item(self):
        self.find_element(SellerPage.add_item_button).click()

    def add_item_by_name(self, item_name, y=0):
        if y == 50:
            raise NameError("Товара нет в списке!!!")
        items = self.find_elements(SellerPage.items)
        x = 0
        for item in items:
            if item_name in item.text:
                try:
                    item.find_element_by_tag_name('button').click()
                except ElementClickInterceptedException:
                    self.driver.execute_script("window.document.body.scrollBy(0, 300)")
                    item.find_element_by_tag_name('button').click()
            else:
                x += 1
        if x == len(items):
            y += 1
            self.driver.execute_script("window.document.body.scrollBy(0, 300)")
            self.add_item_by_name(item_name, y)

    def search_from_seller_page(self, search_req):
        self.click(self.search_input)
        self.input(search_req, self.search_input_second)
