# Отчёт за неделю + Кассовый отчёт + Моментальные + Терминал + Текущая дата
import pytest


@pytest.mark.parametrize('report_type', ["1033"])
def test_report_today_for_the_week_ml(app, report_type):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.select_checkbox_for_the_week()
    app.report.button_get_report()
    app.report.parser_report_text()
    assert "КАССОВЫЙ ОТЧЕТ ЗА НЕДЕЛЮ" in app.report.parser_report_text()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.parser_report_text()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.parser_report_text()
    assert "Продавец: 2000006810-20003511" in app.report.parser_report_text()
    assert "Терминал: 2000006810" in app.report.parser_report_text()
    assert app.report.beginning_of_the_week_C() in app.report.parser_report_text()
    assert app.report.current_day_Po() in app.report.parser_report_text()
    app.report.message_id_32_small_today_for_the_week(report_type)
    app.report.comeback_main_page()