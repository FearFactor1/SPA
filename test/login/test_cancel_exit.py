# Тест: войти в с3, нажать выход, отменить выход



def test_cancel_exit(app2):
    app2.login.correct_user()
    app2.login.enter_button()
    app2.login.exit_cancel_exit()
    assert "Пользователь:" in app2.login.user_in_main_page()
    assert "20003511" in app2.login.user_in_main_page()
    assert "Терминал:" in app2.login.user_in_main_page()
    assert "2000006810" in app2.login.user_in_main_page()
    app2.session.exit_spa()
