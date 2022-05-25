import requests
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, \
    ElementClickInterceptedException
from utils import credentials
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.custom_EC import length_of_the_element_text_not_null, element_has_new_text, pay_button_is_red
from selenium.webdriver.common.keys import Keys


class Executor:
    """Обертка над webdriver, все классы страниц наследуют от него"""

    def __init__(self, driver, ae_buyer_id):
        self.driver = driver
        self.ae_buyer_id = ae_buyer_id

    def has_node(self, locator):
        try:
            self.find_element(locator)
        except:
            return False
        return True

    def scroll_address_slider(self):
        self.driver.execute_script("document.getElementById('bottomSliderChildren').scrollBy(0, 500)")

    def fix(self):
        self.driver.execute_script(f"localStorage.setItem('aer-x-user-id', '{credentials.ae_buyer_id}')")
        self.driver.refresh()

    def reset(self):
        self.driver.execute_script(f"localStorage.removeItem('aer-x-user-id', '{credentials.ae_buyer_id}')")
        self.driver.refresh()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def find_banner(self, locator, first_try=0, max_attempt_to_scroll_down=0):
        if max_attempt_to_scroll_down == 50:
            raise NameError('Пролистали карусель 50 раз - элемент нажать невозможно.')
        element = self.find_element(locator)
        try:
            self.driver.implicitly_wait(3)
            element.click()
            self.driver.implicitly_wait(60)
        except (ElementNotInteractableException, ElementClickInterceptedException):
            if first_try == 0:
                self.driver.execute_script("window.document.getElementsByClassName('swiper-container')[0].scrollBy(300, 0)")
                try:
                    self.driver.implicitly_wait(3)
                    element.click()
                    self.driver.implicitly_wait(60)
                except (ElementNotInteractableException, ElementClickInterceptedException):
                    first_try = 1
                    self.find_banner(locator, first_try)
            else:
                first_try = 1
                max_attempt_to_scroll_down += 1
                self.driver.execute_script("window.document.getElementsByClassName('swiper-container')[0].scrollBy(300, 0)")
                self.find_banner(locator, first_try, max_attempt_to_scroll_down)

    def click(self, locator):
        element = self.find_element(locator)
        try:
            element.click()
        except:
            y_position = int(element.location['y']) - 300
            self.driver.execute_script(f"document.body.scrollBy(0, {y_position})")
            element.click()

    def input(self, text, locator):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text, Keys.ENTER)

    def wait_until_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))

    def wait_until_element_has_new_text(self, locator, old_text):
        WebDriverWait(self.driver, 3).until(element_has_new_text(locator, old_text))

    def wait_until_pay_button_is_red(self, locator):
        WebDriverWait(self.driver,3).until(pay_button_is_red(locator))

    def scroll_from_one_element_to_another(self, first_element, second_element):
        self.driver.scroll((self.find_element(first_element)), (self.find_element(second_element)))

    def get_text(self, locator):
        WebDriverWait(self.driver, 10).until(length_of_the_element_text_not_null(locator))
        return self.find_element(locator).text

    def wait_length_of_the_element_text_not_null(self, locator):
        WebDriverWait(self.driver, 60).until(length_of_the_element_text_not_null(locator))

    def get_text_from_element(self, element):
        return element.text

    def wait_until_element_to_be_on_page(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def wait_until_element_have_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))

    def go_to_start_position(self):
        self.driver.get(credentials.test_url)

    def change_address_through_request(self, address):
        headers = {
            'accept': 'text/plain',
            'x-user-id': f'{self.ae_buyer_id["id"]}',
            'Content-Type': 'application/json-patch+json',
        }
        data = '{}'
        response = requests.post('http://',
                                 headers=headers,data=data)
        if response.json()['data']['address']['place_id'] not in address:
            headers = {
                'accept': 'text/plain',
                'Content-Type': 'application/json-patch+json',
                'x-user-id': f'{self.ae_buyer_id["id"]}'
            }
            data = address.encode('utf-8')
            change_address_req = ''
            requests.post(change_address_req, headers=headers, data=data)
            self.driver.execute_script("window.sessionStorage.removeItem('AER-BUYER_ADDRESS')")
            self.go_to_start_position()
        else:
            self.go_to_start_position()
