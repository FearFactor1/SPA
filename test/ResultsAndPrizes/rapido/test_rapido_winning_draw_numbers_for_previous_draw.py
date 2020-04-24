# зодиак + Выигрышные номера тиража + предыдущий тираж к примеру 130600



def test_rapido_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_rapido()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_130600_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "РАПИДО - Тираж 130600 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "23/04/2020, 15:37:30 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "06 11 18 17 04 16 15 13-04" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()