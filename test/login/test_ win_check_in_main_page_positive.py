# Проверяем выигрышный ли билет по уникальному ключу и если нет, то вместо ошибки отображается 0
import pytest




@pytest.mark.parametrize('ticketid', ["285553976", "34756382"])
def test_win_check_in_main_page_positive(app2, ticketid):
    app2.login.correct_user()
    app2.login.enter_button()
    app2.login.click_show_more_in_main_page()
    app2.login.click_win_check_in_main_page()
    assert app2.login.press_unique_key_positive(ticketid) == app2.login.send_message_id_50_sum_win_positive(ticketid)
    app2.login.close_bonus_modal_phone()
    app2.session.exit_spa()
