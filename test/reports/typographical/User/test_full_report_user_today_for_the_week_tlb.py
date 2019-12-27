# Отчет за неделю + без галочки Кассовый отчёт + Типографские + Пользователь + Текущая неделя


def test_full_report_user_today_for_the_week_tlb(app):
    app.report.open_page_report()
    app.report.select_typographical()
    app.report.select_user()
    app.report.select_checkbox_for_the_week()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.parser_full_report_text_for_typographical()
    assert "ОТЧЕТ ЗА НЕДЕЛЮ" in app.report.parser_full_report_text_for_typographical()
    assert "ПО ТИПОГРАФСКИМ БИЛЕТАМ" in app.report.parser_full_report_text_for_typographical()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.parser_full_report_text_for_typographical()
    assert "Продавец: 2000006810-20003511" in app.report.parser_full_report_text_for_typographical()
    assert "Пользователь: 20003511" in app.report.parser_full_report_text_for_typographical()
    assert app.report.beginning_of_the_week_C() in app.report.parser_full_report_text_for_typographical()
    assert app.report.current_day_Po() in app.report.parser_full_report_text_for_typographical()
    app.report.comeback_main_page()
