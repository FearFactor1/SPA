# рапидо + Результаты тиража + предыдущий тираж к примеру 130600



def test_rapido_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_rapido()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_130600_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "РАПИДО - Тираж 130600 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "23/04/2020, 15:37:30 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "8+1" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "8" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "7+1" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "7" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "6+1" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "6" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5+1" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "4+1" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()
