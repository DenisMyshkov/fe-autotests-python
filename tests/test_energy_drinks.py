import time

from pages.cart import Cart
from pages.main_page import MainPage
from pages.seller_page import SellerPage


def test_bottom_slider_has_info(app, cart_cleaning, make_user_not_adult, pepsi_address):
    app.open_seller_by_name('Pepsi')
    app.search_from_main_page('Энергетики')
    app.add_first_item()
    text = app.get_text(MainPage.bottom_slider)
    expected_text = ['Вам есть 18 лет?',
                     'По закону мы не продаём энергетические напитки несовершеннолетним']
    for i in expected_text:
        assert i in text


def test_item_card_has_opacity_05(app, cart_cleaning, make_user_not_adult, pepsi_address):
    app.open_seller_by_name('Pepsi')
    app.search_from_main_page('Энергетики')
    app.add_first_item()
    app.click(SellerPage.no_button)
    assert '0.5' == app.find_element(SellerPage.add_item_button).value_of_css_property('opacity')


def test_cart_has_info_about_passport(app, cart_cleaning, make_user_not_adult, pepsi_address):
    app.open_seller_by_name('Pepsi')
    app.search_from_main_page('Энергетики')
    app.add_first_item()
    time.sleep(1)
    app.click(SellerPage.yes_button)
    time.sleep(1)
    app.add_first_item()
    app.press_pay_button()
    text = 'По закону мы не продаём энергетические напитки несовершеннолетним. При получении заказа покажите паспорт'
    assert text in app.get_text(Cart.need_passport_info)
