# Отчет за неделю + без галочки Кассовый отчёт + Типографские + Терминал + за предыдущий месяц с 10го


def test_previous_month_full_report_for_the_week_tlb(app):
    app.report.open_page_report()
    app.report.select_typographical()
    app.report.previous_month_date_10()
    app.report.select_checkbox_for_the_week()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.parser_full_report_text_for_typographical()
    assert "ОТЧЕТ ЗА НЕДЕЛЮ" in app.report.parser_full_report_text_for_typographical()
    assert "ПО ТИПОГРАФСКИМ БИЛЕТАМ" in app.report.parser_full_report_text_for_typographical()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.parser_full_report_text_for_typographical()
    assert "Продавец: 2000006810-20003511" in app.report.parser_full_report_text_for_typographical()
    assert "Терминал: 2000006810" in app.report.parser_full_report_text_for_typographical()
    assert app.report.previous_month_C_monday_from_day_10() in app.report.parser_full_report_text_for_typographical()
    assert app.report.previous_month_Po_sunday_from_monday() in app.report.parser_full_report_text_for_typographical()
    app.report.comeback_main_page()