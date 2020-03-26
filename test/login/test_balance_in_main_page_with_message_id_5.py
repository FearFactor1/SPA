# Тест: Заходим на главную страницу спа и проверяем баланс с запросом в гейт message_id=5


def test_show_balance_with__message_id_5(app2):
    app2.login.correct_user()
    app2.login.enter_button()
    app2.login.click_balance_in_main_page()
    assert app2.login.balance_text_in_main_page() == app2.login.send_message_id_5()
    app2.session.exit_spa()