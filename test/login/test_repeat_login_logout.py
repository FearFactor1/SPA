# Тест: Заходим в СПА и выходим затем повторно заходим и выходим в рамках одного запуска


def test_login_logout_and_repeat(app2):
    app2.login.correct_user()
    app2.login.enter_button()
    app2.session.exit_spa()
    app2.login.correct_user()
    app2.login.enter_button()
    app2.session.exit_spa()