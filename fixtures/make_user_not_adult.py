import pytest
import requests
from utils import credentials


@pytest.fixture()
def make_user_not_adult(app):
    requests.post(**{
    'url': '',
    'data': '{\"is_adult\":false}',
    'headers': {
        'accept': 'text/plain',
        'Content-Type': 'application/json-patch+json',
        'x-user-id': f'{app.ae_buyer_id["id"]}'
    }
})
