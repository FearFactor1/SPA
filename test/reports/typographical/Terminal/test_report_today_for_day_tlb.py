# Отчёт за день + Кассовый отчёт + Типографские + Терминал + Текущая дата



def test_report_today_tlb(app):
    app.report.open_page_report()
    app.report.select_typographical()
    app.report.button_get_report()
    app.report.parser_report_text()
    assert "КАССОВЫЙ ОТЧЕТ ЗА ДЕНЬ" in app.report.parser_report_text()
    assert "ПО ТИПОГРАФСКИМ БИЛЕТАМ" in app.report.parser_report_text()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.parser_report_text()
    assert "Продавец: 2000006810-20003511" in app.report.parser_report_text()
    assert "Терминал: 2000006810" in app.report.parser_report_text()
    assert app.report.current_day_C() in app.report.parser_report_text()
    assert app.report.current_day_Po() in app.report.parser_report_text()
    assert 'Продажи' in app.report.parser_report_text()
    assert 'Отмены' in app.report.parser_report_text()
    assert 'Выплаты' in app.report.parser_report_text()
    assert 'ИТОГО ПО КАССЕ' in app.report.parser_report_text()
    app.report.comeback_main_page()