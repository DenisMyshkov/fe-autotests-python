import pytest
from utils import credentials


@pytest.fixture(scope="function", autouse=False)
def one_store_checking(app):
    app.driver.execute_script(f"localStorage.setItem('aer-x-user-id', '{credentials.ae_buyer_id_for_one_store}')")
    app.go_to_start_position()
    yield
    app.driver.execute_script(f"localStorage.setItem('aer-x-user-id', '{credentials.ae_buyer_id}')")
