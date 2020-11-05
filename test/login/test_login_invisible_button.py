# Тест: Кнопка Войти не доступна после кликов на поле логин и пароль


def test_invisible_button(app):
    app.session.exit_spa()
    app.login.invisible_button() # проверка, что кнопка Войти не доступна