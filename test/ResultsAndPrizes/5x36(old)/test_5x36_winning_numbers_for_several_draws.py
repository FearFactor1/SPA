# 5из36(Старая) + Выигрышные номера нескольких тиражей



def test_5x36_winning_numbers_for_several_draws(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_the_winning_numbers_for_several_draws()
    app.ResultAndPrizes.click_ok_in_winning_numbers_for_several_draws_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 5/36 (Старая) - Тираж 10573 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "07/09/2017, 19:00:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "24 04 18 23 05" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 5/36 (Старая) - Тираж 10572 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "07/09/2017, 18:16:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "04 02 20 13 11" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 5/36 (Старая) - Тираж 10571 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "07/09/2017, 18:01:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "23 35 20 03 05" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 5/36 (Старая) - Тираж 10570 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "07/09/2017, 17:46:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "14 16 03 10 13" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 5/36 (Старая) - Тираж 10569 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "07/09/2017, 17:31:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "19 18 01 07 33" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()