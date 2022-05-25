import pytest
from utils import credentials


@pytest.fixture()
def novatorov_address(app):
    app.change_address_through_request(credentials.novatorov_address)


@pytest.fixture()
def pepsi_address(app):
    app.change_address_through_request(credentials.pepsi_address)


@pytest.fixture()
def only_pharma_address(app):
    app.change_address_through_request(credentials.only_pharma_address)
