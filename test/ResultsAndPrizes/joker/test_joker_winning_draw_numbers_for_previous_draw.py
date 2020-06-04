# Джокер + Выигрышные номера тиража + предыдущий тираж к примеру 59587



def test_joker_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_joker()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_59587_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Джокер - Тираж 59587 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "03/06/2020, 15:21:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "03 15 17 04 19 06 31 33 29 02 30 44 37 05 43" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()