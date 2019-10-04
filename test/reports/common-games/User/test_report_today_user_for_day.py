# Отчёт за день + Кассовый отчёт + Обычные + Пользователь + Текущая дата



def test_report_today_user(app):
    app.report.open_page_report()
    app.report.select_user()
    app.report.button_get_report()
    app.report.parser_report_text()
    assert "ОТЧЕТ ЗА ДЕНЬ" in app.report.parser_report_text()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.parser_report_text()
    assert "Продавец: 2000006809-0020003510" in app.report.parser_report_text()
    assert " Пользователь :0020003510" in app.report.parser_report_text()
    assert app.report.current_day_C() in app.report.parser_report_text()
    assert app.report.current_day_Po() in app.report.parser_report_text()
    assert 'Продажи' in app.report.parser_report_text()
    assert 'Отмены' in app.report.parser_report_text()
    assert 'Выплаты' in app.report.parser_report_text()
    assert 'ИТОГО ПО КАССЕ' in app.report.parser_report_text()
    app.report.comeback_main_page()