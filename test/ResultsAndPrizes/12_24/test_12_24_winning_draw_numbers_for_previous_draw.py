# 12/24 + Выигрышные номера тиража + предыдущий тираж к примеру 150597



def test_12_24_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_12_24()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_150597_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 12/24 - Тираж 150597 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "01/06/2020, 12:15:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "14 12 04 11 13 21 06 07 19 16 09 02" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()