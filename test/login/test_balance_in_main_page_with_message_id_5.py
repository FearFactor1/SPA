# Тест: Заходим на главную страницу спа и проверяем баланс с запросом в гейт message_id=5


def test_show_balance_with__message_id_5(app):
    app.login.click_balance_in_main_page()
    assert app.login.balance_text_in_main_page() == app.login.send_message_id_5()