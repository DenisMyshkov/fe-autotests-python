def test_suggests(app, novatorov_address):
    """Проверяем - есть ли блок саджестов"""
    app.open_main_page_search_input()
    assert app.has_suggests_block()
