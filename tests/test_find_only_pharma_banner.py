def test_find_only_pharma_banner(app, only_pharma_address):
    app.open_seller_by_name('Аптека')
    assert app.has_pharma_banner() == 1
