# зодиак + Сумма суперприза



def test_zodiac_sum_superprize(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_zodiac()
    app.ResultAndPrizes.click_sum_superprize()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "СУПЕРПРИЗЫ" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.message_id_33_zodiac_superprizes()
    app.ResultAndPrizes.comeback_main_page()