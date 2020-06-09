# Топ-3 + Результаты тиража + предыдущий тираж к примеру 121750



def test_top_3_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_top_3()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_121750_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ТОП-3 - Тираж 121750 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "09/03/2020, 11:40:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[1]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[2]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[3]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[4]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[5]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[6]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[7]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[8]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[9]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[10]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[11]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[12]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()