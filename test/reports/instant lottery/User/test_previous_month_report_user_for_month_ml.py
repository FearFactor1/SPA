# Отчёт за месяц + с галочкой Кассовый отчёт + Моментальные + Пользователь + предыдущий месяц, к примеру будет 1 число
import pytest



@pytest.mark.parametrize('report_type', ["519"])
def test_previous_month_report_user_for_month_ml(app, report_type):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.select_user()
    app.report.previous_month_date_1()
    app.report.select_checkbox_for_month()
    app.report.button_get_report()
    app.report.parser_report_text()
    assert "КАССОВЫЙ ОТЧЕТ ЗА МЕСЯЦ" in app.report.parser_report_text()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.parser_report_text()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.parser_report_text()
    assert "Продавец: 2000006810-20003511" in app.report.parser_report_text()
    assert "Пользователь: 20003511" in app.report.parser_report_text()
    assert app.report.previous_month_C_day_1() in app.report.parser_report_text()
    assert app.report.previous_month_Po_lastday() in app.report.parser_report_text()
    app.report.message_id_32_previous_month_report_for_month(report_type)
    app.report.comeback_main_page()