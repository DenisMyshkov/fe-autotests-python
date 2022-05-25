import allure
import pytest
import requests
import time
from application.application import Application
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import credentials


@pytest.fixture(scope="class")
def no_login_app(request):
    requests.post(**credentials.clear_cart)
    options = Options()
    options.add_argument("user-agent=AliAppiphone")
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(0, 0)
    driver.set_window_size(300, 880)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(20)
    driver.implicitly_wait(15)
    driver.get(credentials.test_url)
    request.addfinalizer(driver.quit)
    no_login_app = Application(driver)
    return no_login_app
