# Топ-3 + Сумма суперприза



def test_top_3_sum_superprize(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_top_3()
    app.ResultAndPrizes.click_sum_superprize()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "СУПЕРПРИЗЫ" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.message_id_33_top_3_superprizes()
    app.ResultAndPrizes.comeback_main_page()