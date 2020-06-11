# Кено + Выигрышные номера тиража + предыдущий тираж к примеру 151740



def test_keno_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_keno()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_151740_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "КЕНО - Тираж 151740 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "11/06/2020, 09:48:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "01 09 08 07 01 00 05 06 09-08 26 11 31 25 44 75" in app.ResultAndPrizes.parser_report_text_winners()
    assert "45 05 38 18 62 63 19 79 73 23 04 80 74" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()