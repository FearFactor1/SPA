# Кено + Результаты тиража + предыдущий тираж к примеру 151740



def test_keno_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_keno()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_151740_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "КЕНО - Тираж 151740 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "11/06/2020, 09:48:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[1]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[2]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[3]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[4]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[5]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[6]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[25]" and "300" and "2" and "600" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[28]" and "40" and "11" and "440" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[35]" and "20" and "1" and "20" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[39]" and "20" and "1" and "20" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()