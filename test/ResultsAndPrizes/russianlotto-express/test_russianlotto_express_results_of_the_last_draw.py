# «Русское лото Экспресс» + Результаты последнего тиража



def test_russianlotto_express_results_last_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_russianlotto_express()
    app.ResultAndPrizes.click_results_of_the_last_draw()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.message_id_33_russianlotto_express_results_last_draw()
    app.ResultAndPrizes.comeback_main_page()