# Отчёт за месяц + с галочкой Кассовый отчёт + Обычные + Терминал + предыдущий месяц, к примеру будет 1 число



def test_previous_month_report_for_month(app):
    app.report.open_page_report()
    app.report.previous_month_date_1()
    app.report.select_checkbox_for_month()
    app.report.button_get_report()
    app.report.parser_report_text()
    assert "КАССОВЫЙ ОТЧЕТ ЗА МЕСЯЦ" in app.report.parser_report_text()
    assert "ПО ОБЫЧНОЙ ЛОТЕРЕЕ" in app.report.parser_report_text()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.parser_report_text()
    assert "Продавец: 2000006810-20003511" in app.report.parser_report_text()
    assert "Терминал: 2000006810" in app.report.parser_report_text()
    assert app.report.previous_month_C_day_1() in app.report.parser_report_text()
    assert app.report.previous_month_Po_lastday() in app.report.parser_report_text()
    assert 'Продажи' in app.report.parser_report_text()
    assert 'Продажи за бонусы' in app.report.parser_report_text()
    assert 'Отмены' in app.report.parser_report_text()
    assert 'Отмены за бонусы' in app.report.parser_report_text()
    assert 'Выплаты' in app.report.parser_report_text()
    assert 'ИТОГО ПО КАССЕ' in app.report.parser_report_text()
    app.report.comeback_main_page()