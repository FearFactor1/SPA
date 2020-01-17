# 5из36(Старая) + Результаты тиража



def test_5x36_results_draw_current_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 5/36 (Старая) - Тираж 10573 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "07/09/2017, 19:00:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5/5+1" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5/5" and "30676" and "25" and "766900" in app.ResultAndPrizes.parser_report_text_winners()
    assert "4/5" and "2793" and "874" and "2441082" in app.ResultAndPrizes.parser_report_text_winners()
    assert "3/5" and "292" and "8232" and "2403744" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()