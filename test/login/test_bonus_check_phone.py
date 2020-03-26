# Проверка сколько бонусов на телефоне через главное меню в СПА



def test_bonus_check_phone_in_main_page(app2):
    app2.login.correct_user()
    app2.login.enter_button()
    app2.login.click_show_more_in_main_page()
    app2.login.click_bonus_check_in_main_page()
    app2.login.press_phone_bonus()
    assert app2.login.bonus_balance_in_modal_window() == app2.login.send_message_id_64()
    app2.login.click_ok_bonus_modal_window()
    app2.login.close_bonus_modal_phone()
    app2.session.exit_spa()
