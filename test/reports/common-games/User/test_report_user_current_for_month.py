# Отчёт за месяц + с галочкой Кассовый отчёт + Обычные + Пользователь + Текущий месяц



def test_report_user_current_for_month(app):
    app.report.open_page_report()
    app.report.select_user()
    app.report.select_checkbox_for_month()
    app.report.button_get_report()
    app.report.parser_report_text()
    assert "КАССОВЫЙ ОТЧЕТ ЗА МЕСЯЦ" in app.report.parser_report_text()
    assert "ПО ОБЫЧНОЙ ЛОТЕРЕЕ" in app.report.parser_report_text()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.parser_report_text()
    assert "Продавец: 2000006810-20003511" in app.report.parser_report_text()
    assert "Пользователь: 20003511" in app.report.parser_report_text()
    assert app.report.current_month_C() in app.report.parser_report_text()
    assert app.report.current_day_Po() in app.report.parser_report_text()
    assert 'Продажи' in app.report.parser_report_text()
    assert 'Продажи за бонусы' in app.report.parser_report_text()
    assert 'Отмены' in app.report.parser_report_text()
    assert 'Отмены за бонусы' in app.report.parser_report_text()
    assert 'Выплаты' in app.report.parser_report_text()
    assert 'ИТОГО ПО КАССЕ' in app.report.parser_report_text()
    app.report.comeback_main_page()