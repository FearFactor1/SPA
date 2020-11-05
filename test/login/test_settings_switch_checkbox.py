# Проверка отключения и включения настроек спа


def test_settings_switch_checkbox(app):
    app.login.click_show_more_in_main_page()
    app.login.click_settings_in_main_page()
    app.login.click_all_settings()
    app.login.close_bonus_modal_phone()
    app.login.click_settings_in_main_page()
    app.login.click_all_settings()
    app.login.close_bonus_modal_phone()