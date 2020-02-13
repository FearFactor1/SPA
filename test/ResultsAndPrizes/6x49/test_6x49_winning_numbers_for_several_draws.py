# 6из49 + Выигрышные номера нескольких тиражей



def test_6x49_winning_numbers_for_several_draws(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_6x49()
    app.ResultAndPrizes.click_the_winning_numbers_for_several_draws()
    app.ResultAndPrizes.click_ok_for_several_draws_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 6/49 - Тираж 35325 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "18/01/2018, 17:17:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "31 46 40 45 27 36 22" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 6/49 - Тираж 35324 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "18/01/2018, 17:02:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "37 07 15 45 41 43 11" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 6/49 - Тираж 35323 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "18/01/2018, 16:47:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "06 38 09 02 45 44 20" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 6/49 - Тираж 35322 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "18/01/2018, 16:32:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "48 05 24 32 07 19 43" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 6/49 - Тираж 35321 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "18/01/2018, 16:17:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "35 18 48 47 30 03 44" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()