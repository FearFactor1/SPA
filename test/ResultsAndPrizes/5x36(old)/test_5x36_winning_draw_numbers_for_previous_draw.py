# 5из36(Старая) + Выигрышные номера тиража + предыдущий тираж к примеру 10563



def test_5x36_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_10563_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 5/36 (Старая) - Тираж 10563 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "07/09/2017, 16:01:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "32 34 21 36 20" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()
