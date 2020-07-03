# Отчет с начала недели + без галочки Кассовый отчёт + Моментальные + Пользователь + за предыдущий месяц с 10го



def test_previous_month_full_report_user_since_the_beginning_of_the_week_ml(app):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.select_user()
    app.report.previous_month_date_10()
    app.report.select_checkbox_since_the_beginning_of_the_week()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.title_report_for_instant_game()
    assert "ОТЧЕТ С НАЧАЛА НЕДЕЛИ" in app.report.title_report_for_instant_game()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.title_report_for_instant_game()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.title_report_for_instant_game()
    assert "Продавец: 2000006810-20003511" in app.report.title_report_for_instant_game()
    assert "Пользователь: 20003511" in app.report.title_report_for_instant_game()
    assert app.report.previous_month_C_monday_from_day_10() in app.report.title_report_for_instant_game()
    assert app.report.previous_month_Po_sunday_from_monday() in app.report.title_report_for_instant_game()
    app.report.message_id_32_previous_month_beginning_of_the_week_user()
    app.report.comeback_main_page()
