# 4из20 + Результаты нескольких тиражей



def test_4x20_results_for_several_draws(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_4x20()
    app.ResultAndPrizes.click_results_for_several_draws()
    app.ResultAndPrizes.click_ok_for_several_draws_modal_window()
    app.ResultAndPrizes.message_id_33_4x20_results_for_5_draws()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()