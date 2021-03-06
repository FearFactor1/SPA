# Отчет с начала недели + без галочки Кассовый отчёт + Моментальные + Терминал + за предыдущий месяц
import pytest



@pytest.mark.parametrize('report_type', ["1032"])
def test_previous_month_full_report_since_the_beginning_of_the_week_ml(app, report_type):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.previous_month_date_10()
    app.report.select_checkbox_since_the_beginning_of_the_week()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.title_report_for_instant_game()
    assert "ОТЧЕТ С НАЧАЛА НЕДЕЛИ" in app.report.title_report_for_instant_game()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.title_report_for_instant_game()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.title_report_for_instant_game()
    assert "Продавец: 2000006810-20003511" in app.report.title_report_for_instant_game()
    assert "Терминал: 2000006810" in app.report.title_report_for_instant_game()
    assert app.report.previous_month_C_monday_from_day_10() in app.report.title_report_for_instant_game()
    assert app.report.previous_month_Po_sunday_from_monday() in app.report.title_report_for_instant_game()
    app.report.message_id_32_previous_month_beginning_of_the_week(report_type)
    app.report.comeback_main_page()