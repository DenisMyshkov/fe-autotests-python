import pytest
import requests
from utils import credentials


@pytest.fixture()
def cart_cleaning(app):
    requests.post(**{
    'url': '',
    'data': f"{{'cart_id':{app.ae_buyer_id['cart']},'ae_buyer_id':{app.ae_buyer_id['id']}}}",
    'headers': {
        'accept': 'text/plain',
        'Content-Type': 'application/json-patch+json'}
})
