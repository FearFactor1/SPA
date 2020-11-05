# Проверка сколько бонусов на телефоне через главное меню в СПА
import pytest


@pytest.mark.parametrize('PLAYER_INFO', ["9123456789"])
def test_bonus_check_phone_in_main_page(app, PLAYER_INFO):
    app.login.click_show_more_in_main_page()
    app.login.click_bonus_check_in_main_page()
    app.login.press_phone_bonus(PLAYER_INFO)
    assert app.login.bonus_balance_in_modal_window() == app.login.send_message_id_64(PLAYER_INFO)
    app.login.click_ok_bonus_modal_window()
    app.login.close_bonus_modal_phone()