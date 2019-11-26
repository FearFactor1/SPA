# Тест: Ввод логина через экранную клавиатуру



def test_screen_keyboard(app2):
    app2.login.press_keyboard() # ввод логина через экранную клавиатуру
    assert "Столото S3" in app2.wd.title
    app2.login.enter_button()
    assert "Пользователь:" in app2.login.user_in_main_page()
    assert "20003511" in app2.login.user_in_main_page()
    assert "Терминал:" in app2.login.user_in_main_page()
    assert "2000006810" in app2.login.user_in_main_page()
    assert app2.session.assertion_current_page() == "http://localhost:9999/"
    app2.session.exit_spa()