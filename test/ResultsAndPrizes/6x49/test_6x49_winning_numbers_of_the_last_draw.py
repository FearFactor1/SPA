# 6из49 + Выигрышные номера последнего тиража



def test_6x49_winning_numbers_last_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_6x49()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 6/49 - Тираж 35325 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "18/01/2018, 17:17:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "31 46 40 45 27 36 22" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()