from pages.address import Address
from pages.cart import Cart
from pages.checkout import Checkout
from pages.header import Header
from pages.main_page import MainPage
from pages.order_list import OrderList
from pages.search_page import SearchPage
from pages.seller_page import SellerPage
from pages.user_info import UserInfo


class Application(Address, Cart, Checkout, Header, MainPage, OrderList, SearchPage, SellerPage, UserInfo):
    pass
