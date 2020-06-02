# Дуэль + Результаты тиража + предыдущий тираж к примеру 121750



def test_duel_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_duel()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_121750_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ДУЭЛЬ - Тираж 121750 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "02/06/2020, 07:42:30 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[1]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[2]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[3]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[4]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[5]" and "60" and "3" and "180" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[6]" and "60" and "120" and "7200" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[7]" and "30" and "1129" and "33870" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[8]" and "30" and "420" and "12600" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()



