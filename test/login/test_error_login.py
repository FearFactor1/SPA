# Тест: 0051 Неверный идентификатор пользователя терминала


def test_error_login(app):
    app.session.exit_spa()
    app.login.incorrect_user()
    app.login.enter_button()
    assert app.login.err_passwword() == "0051 Неверный идентификатор пользователя терминала (-32000)"
