# 7из49 + Выигрышные номера тиража + предыдущий тираж к примеру 10563



def test_7x49_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_7x49()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_10563_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 7/49 - Тираж 10563 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "15/10/2017, 14:03:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "36 13 10 22 35 04 30" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()