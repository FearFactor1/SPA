# matchball + Результаты последнего тиража



def test_matchball_results_last_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_matchball()
    app.ResultAndPrizes.click_results_of_the_last_draw()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.message_id_33_matchball_results_last_draw()
    app.ResultAndPrizes.comeback_main_page()