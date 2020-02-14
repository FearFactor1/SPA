# зодиак + Результаты тиража + предыдущий тираж к примеру 2000



def test_zodiac_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_zodiac()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_2000_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Зодиак - Тираж 2000 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "04/08/2019, 14:15:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[1]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[2]" and "3118" and "3" and "9354" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[3]" and "323" and "76" and "24548" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[4]" and "50" and "1287" and "64350" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()