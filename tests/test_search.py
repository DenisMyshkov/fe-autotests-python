from flaky import flaky

@flaky(max_runs=3, min_passes=1)
def test_search_by_placeholder(app, cart_cleaning, pepsi_address):
    app.open_main_page_search_input()
    app.use_placeholder()
    app.add_first_item()
    assert app.has_not_empty_cart()
