# Бинго 75 + Выигрышные номера последнего тиража



def test_bingo75_winning_numbers_last_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_bingo75()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.message_id_33_bingo75_winning_numbers_last_draw()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()