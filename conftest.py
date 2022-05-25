pytest_plugins = [
    "fixtures.address_changers",
    "fixtures.app",
    "fixtures.cart_cleaning",
    "fixtures.make_user_not_adult",
    "fixtures.screenshot_when_test_has_failed",
    "fixtures.no_login_app",
    "fixtures.one_store_checking"]


# Обеспечивает корректное отображение кирилических символов
def pytest_make_parametrize_id(config, val):
    return repr(val)
