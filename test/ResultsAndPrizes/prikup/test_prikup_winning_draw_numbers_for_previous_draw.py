# Прикуп + Выигрышные номера тиража + предыдущий тираж к примеру 58570



def test_prikup_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_prikup()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_58570_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ПРИКУП - Тираж 58570 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "15/06/2018, 18:10:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "35 21 20 01 23 32 41 49 27 07 48 08 09 24 10" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()