# Отчет с начала недели + с галочкой Кассовый отчёт + Обычные + Терминал + за предыдущий месяц с 10го



def test_report_since_the_beginning_of_the_week_previous_month(app):
    app.report.open_page_report()
    app.report.previous_month_date_10()
    app.report.select_checkbox_since_the_beginning_of_the_week()
    app.report.button_get_report()
    app.report.parser_report_text()
    assert "КАССОВЫЙ ОТЧЕТ С НАЧАЛА НЕДЕЛИ" in app.report.parser_report_text()
    assert "ПО ОБЫЧНОЙ ЛОТЕРЕЕ" in app.report.parser_report_text()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.parser_report_text()
    assert "Продавец: 2000006810-20003511" in app.report.parser_report_text()
    assert "Терминал: 2000006810" in app.report.parser_report_text()
    assert app.report.previous_month_C_monday_from_day_10() in app.report.parser_report_text()
    assert app.report.previous_month_Po_sunday_from_monday() in app.report.parser_report_text()
    assert 'Продажи' in app.report.parser_report_text()
    assert 'Продажи за бонусы' in app.report.parser_report_text()
    assert 'Отмены' in app.report.parser_report_text()
    assert 'Отмены за бонусы' in app.report.parser_report_text()
    assert 'Выплаты' in app.report.parser_report_text()
    assert 'ИТОГО ПО КАССЕ' in app.report.parser_report_text()
    app.report.comeback_main_page()