# Джокер + Результаты тиража + предыдущий тираж к примеру 59587



def test_joker_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_joker()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_59587_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Джокер - Тираж 59587 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "03/06/2020, 15:21:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[1]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[2]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[3]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[4]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[5]" and "60" and "2" and "120" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[6]" and "30" and "1" and "30" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()