# 12/24 + Результаты тиража + предыдущий тираж к примеру 150597



def test_12_24_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_12_24()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_150597_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "12/24 - Тираж 150597 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "01/06/2020, 12:15:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[1]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[2]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[3]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[4]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[5]" and "30" and "1" and "30" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()