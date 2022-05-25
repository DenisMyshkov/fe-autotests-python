from executor.executor import Executor
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.custom_EC import length_of_the_element_text_not_null


class Checkout(Executor):
    payment_method = (By.XPATH, '//*[@qa-locator-name="qa-checkout-addNewCardButton"]')
    new_card_locator = (By.XPATH, '//*[@qa-locator-name="qa-cardList-addNewCardButton"]')
    card_number = (By.XPATH, '//*[@qa-locator-name="qa-card-cardNumber"]')
    exp_date = (By.XPATH, '//*[@qa-locator-name="qa-card-cardExpDate"]')
    cvv = (By.XPATH, '//*[@qa-locator-name="qa-card-cardCVV"]')
    card_holder_name = (By.XPATH, '//*[@qa-locator-name="qa-card-cardClientName"]')
    save_card = (By.XPATH, '/html/body/div/div/div[1]/div/div/form/div[4]/label/span')
    pay_button = (By.XPATH, '//*[@qa-locator-name="qa-checkout-payButton"]')
    pay_button_in_menu = (By.XPATH, '//*[@qa-locator-name="qa-checkout-userMenu-payButton"]')
    to_order_list = (By.PARTIAL_LINK_TEXT, 'К списку заказов')
    added_card_number_text = '5555 55.. 5599'
    thresholds_class_name = (By.XPATH, '//*[@qa-locator-name="qa-checkout-payButton-threshold"]')

    def add_new_card(self, card):
        self.click(Checkout.cvv)
        self.click(Checkout.exp_date)
        self.input(card[0], Checkout.card_number)
        self.input(card[3], Checkout.card_holder_name)
        self.input(card[1], Checkout.exp_date)
        self.input(card[1], Checkout.exp_date)
        self.input(card[1], Checkout.exp_date)
        self.input(card[2], Checkout.cvv)
        self.input(card[2], Checkout.cvv)
        self.input(card[2], Checkout.cvv)
        self.click(Checkout.save_card)
        self.click(Checkout.pay_button)

    def press_add_new_card(self):
        self.wait_until_element_have_text(Checkout.new_card_locator, 'Оплата новой картой')
        self.click(Checkout.new_card_locator)

    def press_pay_method(self):
        self.wait_length_of_the_element_text_not_null(Checkout.payment_method)
        self.click(Checkout.payment_method)

    def press_pay_button(self):
        self.wait_until_element_to_be_clickable(Checkout.pay_button)
        self.find_element(Checkout.pay_button).click()

    def press_pay_button_in_menu(self):
        self.wait_until_element_to_be_clickable(Checkout.pay_button_in_menu)
        self.find_element(Checkout.pay_button_in_menu).click()

    def press_to_order_list_button(self):
        self.find_element(Checkout.to_order_list).click()

    def add_new_card_and_pay(self, new_card):
        WebDriverWait(self.driver, 15).until(length_of_the_element_text_not_null(Checkout.payment_method))
        self.click(Checkout.payment_method)
        self.click(Checkout.new_card_locator)
        self.input(new_card[0], Checkout.card_number)
        self.click(Checkout.exp_date)
        self.input(new_card[1], Checkout.exp_date)
        self.click(Checkout.cvv)
        self.input(new_card[2], Checkout.cvv)
        self.input(new_card[3], Checkout.card_holder_name)
        self.click(Checkout.save_card)
        self.click(Checkout.pay_button)
        self.click(Checkout.pay_button)
