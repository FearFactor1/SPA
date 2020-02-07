# 4из20 + Результаты тиража + предыдущий тираж к примеру 10563



def test_4x20_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_4x20()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_10563_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 4/20 - Тираж 10563 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "23/04/2018, 19:04:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "4+4" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "4+3" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "4+2" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "4+1" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "4+0" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "3+3" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "3+2" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "3+1" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "3+0" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "2+2" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "2+1" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "2+0" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()