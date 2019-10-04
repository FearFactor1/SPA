# Отчёт за месяц + без галочки Кассовый отчёт + Обычные + Терминал + предыдущий месяц, к примеру будет 1 число



def test_previous_month_full_report_for_month(app):
    app.report.open_page_report()
    app.report.previous_month_date_1()
    app.report.select_checkbox_for_month()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.parser_full_report_text()
    assert "ОТЧЕТ ЗА МЕСЯЦ" in app.report.parser_full_report_text()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.parser_full_report_text()
    assert "Продавец: 2000006809-0020003510" in app.report.parser_full_report_text()
    assert "  Терминал :2000006809" in app.report.parser_full_report_text()
    assert app.report.previous_month_C_day_1() in app.report.parser_full_report_text()
    assert app.report.previous_month_Po_lastday() in app.report.parser_full_report_text()
    app.report.comeback_main_page()
