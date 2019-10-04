# Отчет за неделю + с галочкой Кассовый отчёт + Обычные + Пользователь + за предыдущий месяц


def test_previous_month_report_user_for_the_week(app):
    app.report.open_page_report()
    app.report.select_user()
    app.report.previous_month_date_10()
    app.report.select_checkbox_for_the_week()
    app.report.button_get_report()
    app.report.parser_report_text()
    assert "ОТЧЕТ ЗА НЕДЕЛЮ" in app.report.parser_report_text()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.parser_report_text()
    assert "Продавец: 2000006809-0020003510" in app.report.parser_report_text()
    assert " Пользователь :0020003510" in app.report.parser_report_text()
    assert app.report.previous_month_C_monday_from_day_10() in app.report.parser_report_text()
    assert app.report.previous_month_Po_sunday_from_monday() in app.report.parser_report_text()
    assert 'Продажи' in app.report.parser_report_text()
    assert 'Отмены' in app.report.parser_report_text()
    assert 'Выплаты' in app.report.parser_report_text()
    assert 'ИТОГО ПО КАССЕ' in app.report.parser_report_text()
    app.report.comeback_main_page()