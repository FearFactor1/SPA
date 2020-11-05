# Тест: Ввод логина через экранную клавиатуру


def test_screen_keyboard(app):
    app.session.exit_spa()
    app.login.press_keyboard() # ввод логина через экранную клавиатуру
    assert "Столото S3" in app.wd.title
    app.login.enter_button()
    assert "Пользователь:" in app.login.user_in_main_page()
    assert "20003511" in app.login.user_in_main_page()
    assert "Терминал:" in app.login.user_in_main_page()
    assert "2000006810" in app.login.user_in_main_page()
    assert app.session.assertion_current_page() == "http://qa-slave0.infra.stoloto.su:9999/"