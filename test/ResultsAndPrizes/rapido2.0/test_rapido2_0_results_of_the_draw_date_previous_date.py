# рапидо 2.0 + Результаты тиража по дате + за предыдущий месяц с 10го



def test_rapido2_0_results_draw_date_previous_date(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_rapido2_0()
    app.ResultAndPrizes.click_the_results_of_the_draw_date()
    app.ResultAndPrizes.previous_month_day_10_modal_window()
    app.ResultAndPrizes.assert_previous_month_day_10_input_modal_window()
    app.ResultAndPrizes.click_ok_in_modal_window()
    app.ResultAndPrizes.message_id_33_rapido2_0_results_draw_date_previous_date()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()