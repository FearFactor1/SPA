# 6из45 + Выигрышные номера последних 4 тиражей



def test_6x45_winning_numbers_last_4_draws(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_6x45()
    app.ResultAndPrizes.click_winning_numbers_of_the_last_4_draws()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.message_id_33_6x45_winning_numbers_4_last_draw()
    app.ResultAndPrizes.comeback_main_page()