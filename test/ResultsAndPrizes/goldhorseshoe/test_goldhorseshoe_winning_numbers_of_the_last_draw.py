# Золотая подкова + Выигрышные номера последнего тиража



def test_goldhorseshoe_winning_numbers_last_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_goldhorseshoe()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.message_id_33_goldhorseshoe_winning_numbers_last_draw()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()