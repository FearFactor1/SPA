# Тест: Проверяем отображение информацию о техюподдержке на главной странице СПА


def test_look_support_info(app):
    assert "Телефон службы поддержки" in app.login.support_info_in_main_page()
    assert "+7 (900) 614-55-55" in app.login.support_info_in_main_page()
    assert "Задавайте вопросы по электронной почте" in app.login.support_info_in_main_page()