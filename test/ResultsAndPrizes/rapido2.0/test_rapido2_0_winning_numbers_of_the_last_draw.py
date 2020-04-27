# рапидо 2,0 + Выигрышные номера последнего тиража



def test_rapido2_0_winning_numbers_last_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_rapido2_0()
    app.ResultAndPrizes.button_get_report_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.message_id_33_rapido2_0_last_draw()
    app.ResultAndPrizes.message_id_33_rapido2_0_winning_numbers_last_draw()
    app.ResultAndPrizes.comeback_main_page()