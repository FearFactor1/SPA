# 6из49 + Результаты тиража + предыдущий тираж к примеру 30000



def test_6x49_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_6x49()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_30000_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ЛОТО 6/49 - Тираж 30000 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "22/05/2017, 15:02:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "6/6" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5+1" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "5/6" and "290091" and "3" and "870273" in app.ResultAndPrizes.parser_report_text_winners()
    assert "4/6" and "2708" and "272" and "736576" in app.ResultAndPrizes.parser_report_text_winners()
    assert "3/6" and "150" and "6720" and "1008000" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()