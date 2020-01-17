# 5из36(Старая) + Результаты тиража + предыдущий тираж к примеру 10563



def test_5x36_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_10563_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 5/36 (Старая) - Тираж 10563 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "07/09/2017, 16:01:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5/5+1" and "9713400" and "1" and "9713400" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5/5" and "8000" and "82" and "656000" in app.ResultAndPrizes.parser_report_text_winners()
    assert "4/5" and "800" and "1788" and "1430400" in app.ResultAndPrizes.parser_report_text_winners()
    assert "3/5" and "80" and "18108" and "1448640" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()