# Тест: Проверяем отображение информацию о техюподдержке на главной странице СПА


def test_look_support_info(app2):
    app2.login.correct_user()
    app2.login.enter_button()
    assert "Телефон службы поддержки" in app2.login.support_info_in_main_page()
    assert "+7 (900) 614-55-55" in app2.login.support_info_in_main_page()
    assert "Задавайте вопросы по электронной почте" in app2.login.support_info_in_main_page()
    app2.session.exit_spa()