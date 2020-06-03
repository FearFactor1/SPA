# Прикуп + Результаты тиража + предыдущий тираж к примеру 58570



def test_prikup_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_prikup()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_58570_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ПРИКУП - Тираж 58570 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "15/06/2018, 18:10:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[1]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[2]" and "6000" and "2" and "12000" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[3]" and "600" and "22" and "13200" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[4]" and "180" and "176" and "31680" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[5]" and "60" and "710" and "42600" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()