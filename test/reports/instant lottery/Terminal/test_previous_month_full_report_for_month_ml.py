# Отчёт за месяц + без галочки Кассовый отчёт + Моментальные + Терминал + предыдущий месяц, к примеру будет 1 число
import pytest



@pytest.mark.parametrize('report_type', ["1031"])
def test_previous_month_full_report_for_month_ml(app, report_type):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.previous_month_date_1()
    app.report.select_checkbox_for_month()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.title_report_for_instant_game()
    assert "ОТЧЕТ ЗА МЕСЯЦ" in app.report.title_report_for_instant_game()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.title_report_for_instant_game()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.title_report_for_instant_game()
    assert "Продавец: 2000006810-20003511" in app.report.title_report_for_instant_game()
    assert "Терминал: 2000006810" in app.report.title_report_for_instant_game()
    assert app.report.previous_month_C_day_1() in app.report.title_report_for_instant_game()
    assert app.report.previous_month_Po_lastday() in app.report.title_report_for_instant_game()
    app.report.message_id_32_previous_month_full_report_for_month(report_type)
    app.report.comeback_main_page()
