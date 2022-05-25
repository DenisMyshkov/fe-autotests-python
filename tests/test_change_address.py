from pages.address import Address
from pages.main_page import MainPage


def test_change_address(app, cart_cleaning, pepsi_address):
    app.change_address(Address.novatorov_address)
    app.wait_until_element_to_be_on_page(MainPage.sessionID)
    assert app.get_text(Address.address_input_logged_in) == Address.novatorov_address
