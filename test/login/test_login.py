# Тест: Ввод логина и разлогин



def test_login(app2):
    app2.login.correct_user()
    assert "Столото S3" in app2.wd.title
    app2.login.enter_button()
    app2.login.user_in_main_page()
    assert app2.session.assertion_current_page() == "http://localhost:9999/"
    app2.session.exit_spa()