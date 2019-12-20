# Отчет за неделю + без галочки Кассовый отчёт + Моментальные + Терминал + за предыдущий месяц


def test_previous_month_full_report_for_the_week_ml(app):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.previous_month_date_10()
    app.report.select_checkbox_for_the_week()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.parser_full_report_text_for_instant_game()
    assert "ОТЧЕТ ЗА НЕДЕЛЮ" in app.report.parser_full_report_text_for_instant_game()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.parser_full_report_text_for_instant_game()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.parser_full_report_text_for_instant_game()
    assert "Продавец: 2000006810-20003511" in app.report.parser_full_report_text_for_instant_game()
    assert "Терминал: 2000006810" in app.report.parser_full_report_text_for_instant_game()
    assert app.report.previous_month_C_monday_from_day_10() in app.report.parser_full_report_text_for_instant_game()
    assert app.report.previous_month_Po_sunday_from_monday() in app.report.parser_full_report_text_for_instant_game()
    app.report.comeback_main_page()