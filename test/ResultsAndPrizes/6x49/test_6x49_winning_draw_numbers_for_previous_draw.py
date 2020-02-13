# 6из49 + Выигрышные номера тиража + предыдущий тираж к примеру 30000



def test_6x49_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_6x49()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_30000_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 6/49 - Тираж 30000 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "22/05/2017, 15:02:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "35 21 03 39 31 30 36" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()