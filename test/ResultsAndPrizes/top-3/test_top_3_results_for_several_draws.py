# Топ-3 + Результаты нескольких тиражей



def test_top_3_results_for_several_draws(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_top_3()
    app.ResultAndPrizes.click_results_for_several_draws()
    app.ResultAndPrizes.click_ok_for_several_draws_modal_window()
    app.ResultAndPrizes.message_id_33_top_3_results_for_5_draws()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()