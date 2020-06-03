# Прикуп + Сумма суперприза



def test_prikup_sum_superprize(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_prikup()
    app.ResultAndPrizes.click_sum_superprize()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "СУПЕРПРИЗЫ" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ПРИКУП - Тираж 58571 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "15/06/2018, 18:17:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Категория\nСумма руб." in app.ResultAndPrizes.parser_report_text_winners()
    assert "Суперприз\n200000" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()