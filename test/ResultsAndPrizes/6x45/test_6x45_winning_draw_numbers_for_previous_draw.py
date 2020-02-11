# 6из45 + Выигрышные номера тиража + предыдущий тираж к примеру 9000



def test_6x45_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_6x45()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_9000_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 6/45 - Тираж 9000 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "07/12/2019, 09:32:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "24 19 38 41 33 37" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()