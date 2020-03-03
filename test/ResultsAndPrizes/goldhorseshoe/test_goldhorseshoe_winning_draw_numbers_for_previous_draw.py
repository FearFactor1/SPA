# Золотая подкова  + Выигрышные номера тиража + предыдущий тираж к примеру 1600



def test_goldhorseshoe_winning_draw_numbers_for_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_goldhorseshoe()
    app.ResultAndPrizes.click_winning_draw_numbers()
    app.ResultAndPrizes.select_draw_1600_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.message_id_33_goldhorseshoe_winning_draw_numbers_1600()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "ВЫИГРЫШНЫЕ НОМЕРА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()