# Проверяем 4 негативных сценария:
# 1) Билет без выигрыша 2) Билет отменен 3) Уже выплачено 4) Срок выплаты выигрыша истёк
import pytest




@pytest.mark.parametrize('ticketid', ["289460855", "284875001", "43396325", "9030630"])
def test_win_check_in_main_page_negative(app2, ticketid):
    app2.login.correct_user()
    app2.login.enter_button()
    app2.login.click_show_more_in_main_page()
    app2.login.click_win_check_in_main_page()
    assert app2.login.press_unique_key_negative(ticketid) == app2.login.send_message_id_50_sum_win_negative(ticketid)
    app2.login.close_bonus_modal_phone()
    app2.session.exit_spa()