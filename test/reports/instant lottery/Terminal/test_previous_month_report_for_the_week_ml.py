# Отчет за неделю + с галочкой Кассовый отчёт + Моментальные + Терминал + за предыдущий месяц с 10го
import pytest


@pytest.mark.parametrize('report_type', ["1033"])
def test_previous_month_report_for_the_week_ml(app, report_type):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.previous_month_date_10()
    app.report.select_checkbox_for_the_week()
    app.report.button_get_report()
    app.report.parser_report_text()
    assert "КАССОВЫЙ ОТЧЕТ ЗА НЕДЕЛЮ" in app.report.parser_report_text()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.parser_report_text()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.parser_report_text()
    assert "Продавец: 2000006810-20003511" in app.report.parser_report_text()
    assert "Терминал: 2000006810" in app.report.parser_report_text()
    assert app.report.previous_month_C_monday_from_day_10() in app.report.parser_report_text()
    assert app.report.previous_month_Po_sunday_from_monday() in app.report.parser_report_text()
    app.report.message_id_32_previous_month_small_report_for_the_week(report_type)
    app.report.comeback_main_page()