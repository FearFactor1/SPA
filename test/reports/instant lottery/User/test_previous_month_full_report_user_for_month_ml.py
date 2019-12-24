# Отчёт за месяц + без галочки Кассовый отчёт + Моментальные + Пользователь + предыдущий месяц, к примеру будет 1 число



def test_previous_month_full_report_user_for_month_ml(app):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.select_user()
    app.report.previous_month_date_1()
    app.report.select_checkbox_for_month()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.parser_full_report_text_for_instant_game()
    assert "ОТЧЕТ ЗА МЕСЯЦ" in app.report.parser_full_report_text_for_instant_game()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.parser_full_report_text_for_instant_game()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.parser_full_report_text_for_instant_game()
    assert "Продавец: 2000006810-20003511" in app.report.parser_full_report_text_for_instant_game()
    assert "Пользователь: 20003511" in app.report.parser_full_report_text_for_instant_game()
    assert app.report.previous_month_C_day_1() in app.report.parser_full_report_text_for_instant_game()
    assert app.report.previous_month_Po_lastday() in app.report.parser_full_report_text_for_instant_game()
    app.report.comeback_main_page()