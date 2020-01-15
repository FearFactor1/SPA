# Отчёт за месяц + без галочки Кассовый отчёт + Типографские + Пользователь + предыдущий месяц, к примеру будет 1 число



def test_previous_month_full_report_user_for_month_tlb(app):
    app.report.open_page_report()
    app.report.select_typographical()
    app.report.select_user()
    app.report.previous_month_date_1()
    app.report.select_checkbox_for_month()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.parser_full_report_text_for_typographical()
    assert "ОТЧЕТ ЗА МЕСЯЦ" in app.report.parser_full_report_text_for_typographical()
    assert "ПО ТИПОГРАФСКИМ БИЛЕТАМ" in app.report.parser_full_report_text_for_typographical()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.parser_full_report_text_for_typographical()
    assert "Продавец: 2000006810-20003511" in app.report.parser_full_report_text_for_typographical()
    assert "Пользователь: 20003511" in app.report.parser_full_report_text_for_typographical()
    assert app.report.previous_month_C_day_1() in app.report.parser_full_report_text_for_typographical()
    assert app.report.previous_month_Po_lastday() in app.report.parser_full_report_text_for_typographical()
    app.report.comeback_main_page()