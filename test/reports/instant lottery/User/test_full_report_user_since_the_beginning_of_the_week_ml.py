# Отчет с начала недели + без галочки Кассовый отчёт + Моментальные + Пользователь + Текущая неделя
import pytest



@pytest.mark.parametrize('report_type', ["520"])
def test_full_report_user_since_the_beginning_of_the_week_ml(app, report_type):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.select_user()
    app.report.select_checkbox_since_the_beginning_of_the_week()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.title_report_for_instant_game()
    assert "ОТЧЕТ С НАЧАЛА НЕДЕЛИ" in app.report.title_report_for_instant_game()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.title_report_for_instant_game()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.title_report_for_instant_game()
    assert "Продавец: 2000006810-20003511" in app.report.title_report_for_instant_game()
    assert "Пользователь: 20003511" in app.report.title_report_for_instant_game()
    assert app.report.beginning_of_the_week_C() in app.report.title_report_for_instant_game()
    assert app.report.current_day_Po() in app.report.title_report_for_instant_game()
    app.report.message_id_32_beginning_of_the_week(report_type)
    app.report.comeback_main_page()