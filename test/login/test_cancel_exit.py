# Тест: войти в с3, нажать выход, отменить выход


def test_cancel_exit(app):
    app.login.exit_cancel_exit()
    assert "Пользователь:" in app.login.user_in_main_page()
    assert "20003511" in app.login.user_in_main_page()
    assert "Терминал:" in app.login.user_in_main_page()
    assert "2000006810" in app.login.user_in_main_page()
