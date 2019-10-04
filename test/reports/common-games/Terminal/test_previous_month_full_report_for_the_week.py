# Отчет за неделю + без галочки Кассовый отчёт + Обычные + Терминал + за предыдущий месяц


def test_previous_month_full_report_for_the_week(app):
    app.report.open_page_report()
    app.report.previous_month_date_10()
    app.report.select_checkbox_for_the_week()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.parser_full_report_text()
    assert "ОТЧЕТ ЗА НЕДЕЛЮ" in app.report.parser_full_report_text()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.parser_full_report_text()
    assert "Продавец: 2000006809-0020003510" in app.report.parser_full_report_text()
    assert "  Терминал :2000006809" in app.report.parser_full_report_text()
    assert app.report.previous_month_C_monday_from_day_10() in app.report.parser_full_report_text()
    assert app.report.previous_month_Po_sunday_from_monday() in app.report.parser_full_report_text()
    app.report.comeback_main_page()