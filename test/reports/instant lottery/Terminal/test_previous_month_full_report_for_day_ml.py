# Отчёт за день + без галочки Кассовый отчёт + Моментальные + Терминал + предыдущий месяц, к примеру будет 10 число



def test_previous_month_full_report_ml(app):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.previous_month_date_10()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.title_report_for_instant_game()
    assert "ОТЧЕТ ЗА ДЕНЬ" in app.report.title_report_for_instant_game()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.title_report_for_instant_game()
    assert "ИТОГИ ПО ТЕРМИНАЛУ" in app.report.title_report_for_instant_game()
    assert "Продавец: 2000006810-20003511" in app.report.title_report_for_instant_game()
    assert "Терминал: 2000006810" in app.report.title_report_for_instant_game()
    assert app.report.previous_month_C_day_10() in app.report.title_report_for_instant_game()
    assert app.report.previous_month_Po_day_10() in app.report.title_report_for_instant_game()
    app.report.message_id_32_previous_month_full_report_for_day()
    app.report.comeback_main_page()