# 5из36 + Результаты тиража + предыдущий тираж к примеру 10563



def test_5x36_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_5x36()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_10563_in_draw_numbers()
    app.ResultAndPrizes.select_draw_10563_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 5/36 - Тираж 10563 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "05/09/2017, 12:31:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5/5+1" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5/5" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "4/5" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "3/5" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "2/5" and "80" and "5" and "400" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()