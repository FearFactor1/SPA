# 5из36(Старая) + Результаты тиража по дате + текущая дата



def test_5x36_results_draw_date_current_date(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_the_results_of_the_draw_date()
    app.ResultAndPrizes.click_ok_in_modal_window_current_date()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Тиражей нет" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()