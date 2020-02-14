# 7из49 + Результаты тиража + предыдущий тираж к примеру 10563



def test_7x49_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_7x49()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_10563_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 7/49 - Тираж 10563 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "15/10/2017, 14:03:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "7/7" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "6/7" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5/7" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "4/7" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "3/7" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()