# matchball + Выигрышные номера тиража + предыдущий тираж к примеру 2000



def test_matchball_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_matchball()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_2000_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "МАТЧБОЛ - Тираж 2000 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "24/12/2018, 11:19:29 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "02 11 24 44 20-04" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()