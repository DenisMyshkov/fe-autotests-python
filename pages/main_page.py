from executor.executor import Executor
from pages.search_page import SearchPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import credentials


class MainPage(Executor):
    store_names = {'Самокат': (By.XPATH,'//*[@qa-locator-alias="qa-shopList-shop-samokat"]'),
                   'Ашан': (By.XPATH,'//*[@qa-locator-alias="qa-shopList-shop-auchan"]'),
                   '4 Лапы': (By.XPATH,'//*[@qa-locator-alias="qa-shopList-shop-fourlapy"]'),
                   'ЛеМуррр': (By.XPATH,'//*[@qa-locator-alias="qa-shopList-shop-lemurrr"]'),
                   'Pepsi': (By.XPATH,'//*[@qa-locator-alias="qa-shopList-shop-pepsi"]'),
                   'Аптека': (By.XPATH,'//*[@qa-locator-alias="qa-shopList-shop-vseapteki"]')
                   }
    sessionID = (By.XPATH, '//*[@qa-locator-name="qa-sessionID"]')
    all_stores = (By.XPATH, '//*[@qa-locator-name="qa-shopList-shop"]')
    search = (By.XPATH, '//*[@qa-locator-name="qa-mainSearch"]')
    category = (By.XPATH, '//*[@qa-locator-name="qa-categoryList-category"]')
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
    search_res_item = (By.XPATH, '//*[@qa-locator-name="qa-itemList-item-itemName"]')
    search_input = (By.XPATH, '//*[@qa-locator-name="qa-mainSearch"]')
    search_res_text = (By.XPATH, '//*[contains(text(), {search_req)]')
    add_new_address = (By.XPATH, '//*[@qa-locator-name="qa-userAddressesBottomSlider-addNewAddress"]')
    novatorov_address = 'бульвар Новаторов, 8'
    only_pharma_address = 'Хакасская улица, 1'
    pharma_banner = (By.XPATH, '//*[@qa-locator-name="qa-banners-onlyPharma"]')
    swiper_container = (By.XPATH, '//*[@qa-locator-name="qa-swiper"]')
    bottom_slider = (By.XPATH, '//*[@qa-locator-name="qa-bottomSlider-isAdult"]')
    bottom_slider_content = (By.ID, 'bottomSliderContent')
    stores_list_loading_sign = (By.XPATH, '//*[contains(text(), "Загрузка списка магазинов")]')

    def open_main_page_search_input(self):
        self.find_element(MainPage.search_input).click()

    def get_selected_address_name(self):
        address = self.find_element(MainPage.address_input_logged_in).text
        return address

    def open_seller_by_name(self, store_name):
        text_in_search_placeholder = self.get_text(MainPage.search)
        if self.find_element(self.store_names.get(store_name)).value_of_css_property('background-color') != 'rgba(255, 255, 255, 1)':
            self.click(self.store_names.get(store_name))
            self.wait_until_element_has_new_text(MainPage.search, text_in_search_placeholder)

    def check_stores_available(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until_not(EC.presence_of_element_located(MainPage.stores_list_loading_sign))
        wait.until(EC.presence_of_all_elements_located)
        stores_count = len(self.find_elements(MainPage.all_stores))
        return stores_count

    def check_map_opens_if_not_logged_in(self):
        assert EC.url_to_be(f'{credentials.test_url}/?mapSearch=1')
        assert EC.presence_of_all_elements_located

    def has_pharma_banner(self):
        # return self.has_node(MainPage.pharma_banner)
        return len(self.find_element(MainPage.pharma_banner))

    def search_from_main_page(self, search_req):
        self.click(MainPage.search)
        self.input(search_req, SearchPage.search_input)

    def check_of_categories(self):
        """Проверяет после открытия главной есть ли на ней Категории. Если нет - возвращает False"""
        return False if len(self.find_elements(MainPage.category)) == 0 else True

    def enter_address_from_main_page_login(self, address):
        self.wait_until_element_to_be_clickable(MainPage.address_input_logged_in)
        self.click(MainPage.address_input_logged_in)
        self.driver.get(f'{credentials.test_url}/?mapSearch=1')
        self.input(address, MainPage.address_input)
        address = MainPage.address_moscow
        self.wait_until_element_to_be_clickable(address)
        self.click(address)
        self.wait_until_element_to_be_clickable(MainPage.address_confirm_btn)
        self.click(MainPage.address_confirm_btn)

    def search_by_suggest(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(MainPage.search))
        self.click(MainPage.search)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.url_to_be(f'{credentials.test_url}/search'))
        self.click(SearchPage.search_history_item)
        wait.until_not(EC.visibility_of_element_located(MainPage.stores_list_loading_sign))
