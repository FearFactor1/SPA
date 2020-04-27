# рапидо 2.0 + Выигрышные номера тиража + предыдущий тираж к примеру 10563



def test_rapido2_0_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_rapido2_0()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_10563_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "РАПИДО 2 - Тираж 10563 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "28/10/2019, 01:05:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "06 15 01 02 14 05 08 18-04" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()