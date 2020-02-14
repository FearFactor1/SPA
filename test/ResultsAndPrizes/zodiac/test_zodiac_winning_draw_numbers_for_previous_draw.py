# зодиак + Выигрышные номера тиража + предыдущий тираж к примеру 2000



def test_zodiac_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_zodiac()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_2000_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Зодиак - Тираж 2000 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "04/08/2019, 14:15:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "26-12-45-04" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()