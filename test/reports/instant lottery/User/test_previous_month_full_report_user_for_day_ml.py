# Отчёт за день + без галочки Кассовый отчёт + Моментальные + Пользователь + предыдущий месяц, к примеру будет 10 число
import pytest



@pytest.mark.parametrize('report_type', ["518"])
def test_previous_month_full_report_user_ml(app, report_type):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.select_user()
    app.report.previous_month_date_10()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.title_report_for_instant_game()
    assert "ОТЧЕТ ЗА ДЕНЬ" in app.report.title_report_for_instant_game()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.title_report_for_instant_game()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.title_report_for_instant_game()
    assert "Продавец: 2000006810-20003511" in app.report.title_report_for_instant_game()
    assert "Пользователь: 20003511" in app.report.title_report_for_instant_game()
    assert app.report.previous_month_C_day_10() in app.report.title_report_for_instant_game()
    assert app.report.previous_month_Po_day_10() in app.report.title_report_for_instant_game()
    app.report.message_id_32_previous_month_full_report_for_day(report_type)
#    app.report.message_id_32_previous_month_full_report_for_day_user()
    app.report.comeback_main_page()