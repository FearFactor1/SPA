# Дуэль + Выигрышные номера тиража + предыдущий тираж к примеру 121750



def test_duel_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_duel()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_121750_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ДУЭЛЬ - Тираж 121750 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "02/06/2020, 07:42:30 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "21 17-17 19" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()