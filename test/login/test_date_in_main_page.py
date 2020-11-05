# Тест: проверка даты и время на главной страницы


def test_datetime_in_main_page(app):
    app.login.data_in_main_page()