# Бинго 75 + Результаты тиража + предыдущий тираж к примеру 2000



def test_bingo75_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_bingo75()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_2000_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.message_id_33_bingo75_results_draw_2000()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()