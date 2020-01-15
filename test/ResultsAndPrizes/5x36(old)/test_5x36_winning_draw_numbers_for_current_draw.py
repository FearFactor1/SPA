# 5из36(Старая) + Выигрышные номера тиража



def test_5x36_winning_draw_numbers(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 5/36 (Старая) - Тираж 10573 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "07/09/2017, 19:00:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "24 04 18 23 05" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()