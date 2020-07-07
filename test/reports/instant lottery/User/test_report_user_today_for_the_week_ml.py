# Отчет за неделю + с галочкой Кассовый отчёт + Моментальные + Пользователь + Текущая неделя
import pytest


@pytest.mark.parametrize('report_type', ["521"])
def test_report_user_today_for_the_week_ml(app, report_type):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.select_user()
    app.report.select_checkbox_for_the_week()
    app.report.button_get_report()
    app.report.parser_report_text()
    assert "КАССОВЫЙ ОТЧЕТ ЗА НЕДЕЛЮ" in app.report.parser_report_text()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.parser_report_text()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.parser_report_text()
    assert "Продавец: 2000006810-20003511" in app.report.parser_report_text()
    assert "Пользователь: 20003511" in app.report.parser_report_text()
    assert app.report.beginning_of_the_week_C() in app.report.parser_report_text()
    assert app.report.current_day_Po() in app.report.parser_report_text()
    app.report.message_id_32_small_today_for_the_week(report_type)
    app.report.comeback_main_page()