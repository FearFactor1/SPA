# Тест: Заходим в СПА и выходим затем повторно заходим и выходим в рамках одного запуска


def test_login_logout_and_repeat(app):
    app.session.exit_spa()
    app.login.correct_user()
    app.login.enter_button()
    app.session.exit_spa()
    app.login.correct_user()
    app.login.enter_button()
    app.session.exit_spa()