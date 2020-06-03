# Прикуп + Выигрышные номера нескольких тиражей



def test_prikup_winning_numbers_for_several_draws(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_prikup()
    app.ResultAndPrizes.click_the_winning_numbers_for_several_draws()
    app.ResultAndPrizes.click_ok_for_several_draws_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ПРИКУП - Тираж 58571 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "15/06/2018, 18:17:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "13 48 18 29 24 33 32 17 08 12 46 37 47 39 51" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ПРИКУП - Тираж 58570 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "15/06/2018, 18:10:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "35 21 20 01 23 32 41 49 27 07 48 08 09 24 10" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ПРИКУП - Тираж 58569 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "15/06/2018, 17:50:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "03 10 21 07 18 15 30 25 40 11 22 12 46 02 27" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ПРИКУП - Тираж 58568 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "15/06/2018, 17:42:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "21 14 23 19 39 10 08 01 41 31 47 16 26 34 06" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ПРИКУП - Тираж 58567 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "15/06/2018, 17:30:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "28 41 10 27 36 35 50 30 52 01 04 33 44 15 20" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()