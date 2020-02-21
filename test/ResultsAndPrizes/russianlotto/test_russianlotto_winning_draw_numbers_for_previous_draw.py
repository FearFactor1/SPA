# русское лото  + Выигрышные номера тиража + предыдущий тираж к примеру 2000



def test_russianlotto_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_russianlotto()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_2000_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.message_id_33_russianlotto_winning_draw_numbers_2000()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()
