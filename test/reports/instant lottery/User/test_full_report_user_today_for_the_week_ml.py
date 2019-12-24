# Отчет за неделю + без галочки Кассовый отчёт + Моментальные + Пользователь + Текущая неделя


def test_full_report_user_today_for_the_week_ml(app):
    app.report.open_page_report()
    app.report.select_instant_lottery()
    app.report.select_user()
    app.report.select_checkbox_for_the_week()
    app.report.without_checkbox_cash_report()
    app.report.button_get_report()
    app.report.parser_full_report_text_for_instant_game()
    assert "ОТЧЕТ ЗА НЕДЕЛЮ" in app.report.parser_full_report_text_for_instant_game()
    assert "ПО МОМЕНТЛЬНОЙ ЛОТЕРЕЕ" in app.report.parser_full_report_text_for_instant_game()
    assert "ИТОГИ ПО ПОЛЬЗОВАТЕЛЮ" in app.report.parser_full_report_text_for_instant_game()
    assert "Продавец: 2000006810-20003511" in app.report.parser_full_report_text_for_instant_game()
    assert "Пользователь: 20003511" in app.report.parser_full_report_text_for_instant_game()
    assert app.report.beginning_of_the_week_C() in app.report.parser_full_report_text_for_instant_game()
    assert app.report.current_day_Po() in app.report.parser_full_report_text_for_instant_game()
    app.report.comeback_main_page()
