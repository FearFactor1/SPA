# Отчет с начала недели + без галочки Кассовый отчёт + Обычные + Пользователь + Текущая неделя



def test_full_report_user_since_the_beginning_of_the_week(app):
    app.report.open_page_report()
    app.report.select_user()
    app.report.select_checkbox_since_the_beginning_of_the_week()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.parser_full_report_text()
    assert "ОТЧЕТ С НАЧАЛА НЕДЕЛИ" in app.report.parser_full_report_text()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.parser_full_report_text()
    assert "Продавец: 2000006809-0020003510" in app.report.parser_full_report_text()
    assert " Пользователь :0020003510" in app.report.parser_full_report_text()
    assert app.report.beginning_of_the_week_C() in app.report.parser_full_report_text()
    assert app.report.current_day_Po() in app.report.parser_full_report_text()
    app.report.comeback_main_page()