# Проверка отключения и включения настроек спа



def test_settings_switch_checkbox(app2):
    app2.login.correct_user()
    app2.login.enter_button()
    app2.login.click_show_more_in_main_page()
    app2.login.click_settings_in_main_page()
    app2.login.click_all_settings()
    app2.login.close_bonus_modal_phone()
    app2.login.click_settings_in_main_page()
    app2.login.click_all_settings()
    app2.login.close_bonus_modal_phone()
    app2.session.exit_spa()