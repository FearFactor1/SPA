# Отчёт за день + без галочки Кассовый отчёт + Моментальные + Пользователь + Текущая дата



def test_full_report_today_user_ml(app):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.select_user()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.title_report_for_instant_game()
    assert "ОТЧЕТ ЗА ДЕНЬ" in app.report.title_report_for_instant_game()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.title_report_for_instant_game()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.title_report_for_instant_game()
    assert "Продавец: 2000006810-20003511" in app.report.title_report_for_instant_game()
    assert "Пользователь: 20003511" in app.report.title_report_for_instant_game()
    assert app.report.current_day_C() in app.report.title_report_for_instant_game()
    assert app.report.current_day_Po() in app.report.title_report_for_instant_game()
    app.report.message_id_32_report_today_user_ml()
    app.report.comeback_main_page()
