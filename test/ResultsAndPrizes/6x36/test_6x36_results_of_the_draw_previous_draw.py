# 6 из 36 + Результаты тиража + предыдущий тираж к примеру 1600



def test_6x36_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_6x36()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_1600_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.message_id_33_6x36_results_draw_1600()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()