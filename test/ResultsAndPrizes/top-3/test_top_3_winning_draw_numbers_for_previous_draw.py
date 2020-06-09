# Топ-3 + Выигрышные номера тиража + предыдущий тираж к примеру 121750



def test_top_3_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_top_3()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_121750_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "ТОП-3 - Тираж 121750 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "09/03/2020, 11:40:00 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "02 04 03" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Тур 1: 09 01 05 03 08 04 08 06 00" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()