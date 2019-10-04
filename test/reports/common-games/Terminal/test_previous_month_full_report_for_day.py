# Отчёт за день + без галочки Кассовый отчёт + Обычные + Терминал + предыдущий месяц, к примеру будет 10 число



def test_previous_month_full_report(app):
    app.report.open_page_report()
    app.report.previous_month_date_10()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.parser_full_report_text()
    assert "ОТЧЕТ ЗА ДЕНЬ" in app.report.parser_full_report_text()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.parser_full_report_text()
    assert "Продавец: 2000006809-0020003510" in app.report.parser_full_report_text()
    assert "  Терминал :2000006809" in app.report.parser_full_report_text()
    assert app.report.previous_month_C_day_10() in app.report.parser_full_report_text()
    assert app.report.previous_month_Po_day_10() in app.report.parser_full_report_text()
    app.report.comeback_main_page()