import random
from executor.executor import Executor
from selenium.webdriver.common.by import By


class Address(Executor):
    address_clear = (By.XPATH, '//*[@qa-locator-name="qa-mapBottomSlider-address-clearButton"]')
    address_initial = (By.XPATH, '//*[@qa-locator-name="qa-mapData-clientAddress"]')
    address_input = (By.XPATH, '//*[@qa-locator-name="qa-mapBottomSlider-address-input"]')
    address_suggestion_default = (By.XPATH, '//*[@qa-locator-name="qa-mapBottomSlider-address-addressSuggestion"]')
    address_suggestion_single = (By.XPATH, '//div[text()="улица Охотный ряд, 1"]')
    address_suggestion_empty = (By.XPATH, '//div[text()="улица Новаторов, 1"]')
    address_confirm_btn = (By.XPATH, '//*[@qa-locator-name="qa-mapData-hereButton"]')
    address_moscow = (By.XPATH, '//*[contains(text(), "Москва, Россия")]')
    address_input_logged_in = (By.XPATH, '//*[@qa-locator-name="qa-header-headerMiddle-addressPlate"]')
    new_address_btn = (By.XPATH, '//*[contains(text(), "Добавить адрес")]')
    search_input = (By.XPATH, '//*[@qa-locator-name="qa-mainSearch"]')
    search_res_text = (By.XPATH, '//*[contains(text(), {search_req)]')
    add_new_address = (By.XPATH, '//*[@qa-locator-name="qa-userAddressesBottomSlider-addNewAddress"]')
    novatorov_address = 'бульвар Новаторов, 8'
    only_pharma_address = 'Хакасская улица, 1'
    pepsi_address = 'улица Трофимова, 25'


    def change_address(self, address):
        # Сразу после открытия главной в текущем адресе отображается "Добавить адрес" и нажатие в этот момент
        # не дает результата. Нужно ждать пока с бэка придет текущий адрес и надпись смениться на него.
        while self.get_text(Address.address_input_logged_in) == 'Добавить адрес':
            True
        # Проверяем что текущий адрес не совпадает с тем, на который хотим сменить
        if address != self.get_text(Address.address_input_logged_in):
            # Тапаем по полю текущего адреса
            self.click(Address.address_input_logged_in)
            # Тапаем по кнопка Добавить адрес
            self.click(Address.add_new_address)
            # Сразу после открытия страницы ввода нового адреса, поле ввода пустое, затем в поле ввода отображается
            # надпись "Уточните адрес" - нажатие в этот момент не дает результата. Нужно ждать пока с бэка придет
            # текущая геолокация и только потом тапать по полю ввода адреса
            # while len(self.get_text(Address.address_initial)) == 0 or self.get_text(Address.address_initial) == 'Уточните адрес':
            #     True
            # Тапаем по полю ввода адреса
            self.click(Address.address_initial)
            # Тапаем кнопку очистки адреса
            self.click(Address.address_clear)
            # Вводим новый адрес
            self.input(address, Address.address_input)
            # Тапаем по первому саджесту
            self.click(Address.address_suggestion_default)
            # Сразу после тапа по саджесту в поле адреса отображается надпись "Уточните адрес" - нажатие в этот
            # момент не дает результата. Нужно ждать пока с бэка придет новый адрес (тот который соответствует
            # выбранному саджесту)
            while self.get_text(Address.address_confirm_btn) == 'Уточнить адрес':
                True
            # Тапаем кнопку Я здесь (подтверждаем новый адрес)
            self.click(Address.address_confirm_btn)

    def use_random_address(self):
        list_of_addresses = [Address.pepsi_address, Address.novatorov_address, Address.only_pharma_address]
        current_address = self.get_text(Address.address_input_logged_in)
        if current_address not in list_of_addresses:
            na = random.choice(list_of_addresses)
            self.change_address(na)
        else:
            list_of_addresses.remove(current_address)
            na = random.choice(list_of_addresses)
            self.change_address(na)

        return na
