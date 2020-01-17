# 5из36(Старая) + Сумма суперприза



def test_5x36_sum_superprize(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_sum_superprize()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "СУПЕРПРИЗЫ" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 5/36 (Старая) - Тираж 10573 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "07/09/2017, 19:00:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Категория\nСумма руб." in app.ResultAndPrizes.parser_report_text_winners()
    assert "Суперприз\n1000000" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()