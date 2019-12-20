# Отчёт за месяц + без галочки Кассовый отчёт + Моментальные лотереи + Терминал + Текущий месяц



def test_full_report_current_for_month_ml(app):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.without_checkbox_cash_report()
    app.report.select_checkbox_for_month()
    app.report.button_get_report()
    app.report.parser_full_report_text_for_instant_game()
    assert "ОТЧЕТ ЗА МЕСЯЦ" in app.report.parser_full_report_text_for_instant_game()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.parser_full_report_text_for_instant_game()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.parser_full_report_text_for_instant_game()
    assert "Продавец: 2000006810-20003511" in app.report.parser_full_report_text_for_instant_game()
    assert "Терминал: 2000006810" in app.report.parser_full_report_text_for_instant_game()
    assert app.report.current_month_C() in app.report.parser_full_report_text_for_instant_game()
    assert app.report.current_day_Po() in app.report.parser_full_report_text_for_instant_game()
    app.report.comeback_main_page()