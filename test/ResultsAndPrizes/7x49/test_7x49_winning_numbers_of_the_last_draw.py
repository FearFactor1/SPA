# 7из49 + Выигрышные номера последнего тиража



def test_7x49_winning_numbers_last_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_7x49()
    app.ResultAndPrizes.button_get_report_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.message_id_33_7x49_last_draw()
    app.ResultAndPrizes.message_id_33_7x49_winning_numbers_last_draw()
    app.ResultAndPrizes.comeback_main_page()