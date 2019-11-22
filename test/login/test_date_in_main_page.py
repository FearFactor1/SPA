# Тест: проверка даты и время на главной страницы

def test_datetime_in_main_page(app2):
    app2.login.correct_user()
    app2.login.enter_button()
    app2.login.data_in_main_page()
    app2.session.exit_spa()
