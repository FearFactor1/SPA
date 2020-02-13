# 6из49 + Результаты тиража



def test_5x36_results_draw_current_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_6x49()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 6/49 - Тираж 35325 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "18/01/2018, 17:17:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "6/6" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5+1" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5/6" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "4/6" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "3/6" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()
