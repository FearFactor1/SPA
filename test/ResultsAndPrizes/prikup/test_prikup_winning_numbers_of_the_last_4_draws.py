# Прикуп + Выигрышные номера последних 4 тиражей



def test_prikup_winning_numbers_last_4_draws(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_prikup()
    app.ResultAndPrizes.click_winning_numbers_of_the_last_4_draws()
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
    app.ResultAndPrizes.comeback_main_page()