# Дуэль + Выигрышные номера последнего тиража



def test_duel_winning_numbers_last_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_duel()
    app.ResultAndPrizes.button_get_report_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.message_id_33_duel_last_draw()
    app.ResultAndPrizes.message_id_33_duel_winning_numbers_last_draw()
    app.ResultAndPrizes.comeback_main_page()