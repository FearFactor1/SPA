# matchball + Результаты тиража + предыдущий тираж к примеру 2000



def test_matchball_results_draw_previous_draw(app):
    app.ResultAndPrizes.open_page_results_and_prizes()
    app.ResultAndPrizes.click_game_matchball()
    app.ResultAndPrizes.click_the_results_of_the_draw()
    app.ResultAndPrizes.select_draw_2000_in_draw_numbers()
    app.ResultAndPrizes.click_ok_in_winning_draw_numbers_modal_window()
    app.ResultAndPrizes.button_get_report_winners()
    app.ResultAndPrizes.parser_report_text_winners()
    assert "РЕЗУЛЬТАТЫ ТИРАЖА" in app.ResultAndPrizes.parser_report_text_winners()
    assert "МАТЧБОЛ - Тираж 2000 :" in app.ResultAndPrizes.parser_report_text_winners()
    assert "24/12/2018, 11:19:29 ЛОК" in app.ResultAndPrizes.parser_report_text_winners()
    assert "Кат." and "Выигрыш руб." and "Кол-во" and "Всего" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[1]" and "0" and "0" and "0" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[2]" and "27898654" and "1" and "27898654" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[3]" and "58123" and "64" and "3719872" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[4]" and "25768" and "794" and "20459792" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[5]" and "5362" and "3469" and "18600778" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[6]" and "517" and "36028" and "18626476" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[7]" and "260" and "50121" and "13031460" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[8]" and "108" and "258339" and "27900612" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[9]" and "61" and "427814" and "26096654" in app.ResultAndPrizes.parser_report_text_winners()
    assert "[10]" and "50" and "513002" and "25650100" in app.ResultAndPrizes.parser_report_text_winners()
    app.ResultAndPrizes.comeback_main_page()