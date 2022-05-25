import os

import allure
import pytest
import requests
import time

from selenium.webdriver.common.by import By

from application.application import Application
from fixtures.net_log_creator import net_log_creator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import credentials

name_for_bs = f'new_new_main {time.ctime()} {os.getenv("PYTEST_XDIST_WORKER")}'

caps = {
    'os_version': '10',
    'os': 'Windows',
    'resolution': '1920x1080',
    'browser': 'chrome',
    'browser_version': 'latest',
    'name': f'{name_for_bs}',
    'build': 'python_battle',
    'browserstack.networkLogs': 'true',

    'browserstack.local': 'true',
    'acceptSslCerts': 'true'
}
arguments = ["start-maximized",
             "enable-automation",
             "--no-sandbox",
             "--disable-infobars",
             "--disable-dev-shm-usage",
             "--disable-browser-side-navigation",
             "--disable-gpu",
             "--user-agent=AliAppIpod AER",
             '--ignore-ssl-errors=yes',
             '--ignore-certificate-errors']

experimental_options = [["mobileEmulation", {"deviceName": "Pixel 2"}],
                        ['w3c', False],
                        ["prefs", {"profile.default_content_setting_values.geolocation": 1}]]


@pytest.fixture(scope="session")
def app():
    worker = os.getenv("PYTEST_XDIST_WORKER")
    requests.post(**{
        'url': '',
        'data': f"{{'cart_id':{credentials.ae_buyer_id[worker]['cart']},'ae_buyer_id':{credentials.ae_buyer_id[worker]['id']}}}",
        'headers': {
            'accept': 'text/plain',
            'Content-Type': 'application/json-patch+json'}})
    options = Options()
    for argument in arguments:
        options.add_argument(argument)
    for option in experimental_options:
        options.add_experimental_option(*option)
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(0, 0)
    driver.set_window_size(500, 1044)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(20)
    driver.implicitly_wait(60)
    driver.get(credentials.test_url)
    driver.execute_script(f"localStorage.setItem('aer-x-user-id', '{credentials.ae_buyer_id[worker]['id']}')")
    driver.refresh()
    sessionID = driver.find_element(By.XPATH, '//*[@qa-locator-name="qa-sessionID"]').text
    application = Application(driver, credentials.ae_buyer_id[worker])
    application.ae_buyer_id = credentials.ae_buyer_id[worker]
    yield application
    session_id = driver.session_id
    driver.quit()
    net_log = net_log_creator(sessionID, credentials.ae_buyer_id[worker]["id"], session_id, name_for_bs)
    allure.attach(net_log, name="HTML attachment", attachment_type='text/html')
