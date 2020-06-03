# Прикуп + Выигрышные номера тиража



def test_prikup_winning_draw_numbers(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_prikup()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ПРИКУП - Тираж 58571 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "15/06/2018, 18:17:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "13 48 18 29 24 33 32 17 08 12 46 37 47 39 51" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()