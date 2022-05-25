from executor.executor import Executor
from selenium.webdriver.common.by import By


class Cart(Executor):
    promocode_input = (By.XPATH, '//*[@qa-locator-name="qa-cart-promocode-input"]')
    accept_promo_button = (By.XPATH, '//*[@qa-locator-name = "qa-cart-promocode-applyCode"]')
    total_sum = (By.XPATH, '//*[@qa-locator-name = "qa-cart-cartTotalPrice"]')
    to_checkout_button = (By.XPATH, '//*[@qa-locator-name="qa-checkout-payButton"]')
    discount_sum = (By.XPATH, '//*[@qa-locator-name = "qa-cart-promocode-discountSum"]')
    checkout_button = (By.PARTIAL_LINK_TEXT, '//div[text()="Продолжить"]')
    item_quantity_plus = (By.XPATH, '//*[@qa-locator-name = "qa-cart-item-itemQuantity-plus"]')
    need_passport_info = (By.XPATH, '//*[@qa-locator-name = "qa-cart-needPassportInfo"]')  # TODO присвоить элементу локатор
    item_total_sum = (By.XPATH, '//*[@qa-locator-name = "qa-cart-item-itemTotalPrice"]')

    def has_not_empty_cart(self):
        return self.has_node(Cart.to_checkout_button)

    def get_cart_plate_text(self):
        text = self.find_element(Cart.to_checkout_button).text.split(' ')
        return text[1]

    def get_total_sum(self):
        element = self.find_element(Cart.total_sum)
        if len(element.text) == 0:
            self.wait_length_of_the_element_text_not_null(Cart.total_sum)
        return element.text

    def get_item_total_sum(self):
        text = self.get_text(Cart.item_total_sum)
        return text

    def input_valid_promocode(self, promotion):
        self.input(promotion, Cart.promocode_input)
        self.click(Cart.accept_promo_button)
        assert len(self.get_text(Cart.discount_sum)) > 0

    def open_checkout(self):
        self.find_element(Cart.to_checkout_button).click()

    def wait_until_pay_button_is_clickable(self):
        self.wait_until_pay_button_is_red(Cart.to_checkout_button)
