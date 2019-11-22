# Тест: 0051 Неверный идентификатор пользователя терминала


def test_error_login(app2):
    app2.login.incorrect_user()
    app2.login.enter_button()
    assert app2.login.err_passwword() == "-32604 0051 Неверный идентификатор пользователя терминала"
