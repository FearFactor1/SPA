# Проверяем 4 негативных сценария:
# 1) Билет без выигрыша 2) Билет отменен 3) Уже выплачено 4) Срок выплаты выигрыша истёк
import pytest


@pytest.mark.parametrize('ticketid', ["5010553972", "5009047885", "43396325", "9030630"])
def test_win_check_in_main_page_negative(app, ticketid):
    app.login.click_show_more_in_main_page()
    app.login.click_win_check_in_main_page()
    assert app.login.press_unique_key_negative(ticketid) == app.login.send_message_id_50_sum_win_negative(ticketid)
    app.login.close_bonus_modal_phone()
