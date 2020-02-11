# 6из45 + Результаты тиража + предыдущий тираж к примеру 9000



def test_6x45_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_6x45()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_9000_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 6/45 - Тираж 9000 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "07/12/2019, 09:32:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "6/6" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5/6" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "4/6" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "3/6" and "788" and "596" and "469648" in app.ResultAndPrizes.parser_report_text_winners()
    assert "2/6" and "100" and "8387" and "838700" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()