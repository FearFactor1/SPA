# 4из20 + Выигрышные номера тиража + предыдущий тираж к примеру 10563



def test_4x20_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_4x20()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_10563_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 4/20 - Тираж 10563 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "23/04/2018, 19:04:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "18 10 14 02-06 11 16 02" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()