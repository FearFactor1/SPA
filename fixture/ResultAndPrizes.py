from datetime import datetime, timedelta
from requests import post
from requests.auth import HTTPBasicAuth
from fixture.messages import MessageID
import re



# ----------- Глобальные переменные:

login = "s3_http_access"
password = "ambush!Tidy4"
auth = (login, password)
TERMINAL_ID = "2000006810"
LOGIN = "20003511"
PASSWORD = "75374377"
draw_id = '<draw_id>(.*?)</draw_id>'
win_numbers = '<win_numbers>(.*?)</win_numbers>'
winners_count = '<winners_count>(.*?)</winners_count>'
winning_amount = '<winning_amount>(.*?)</winning_amount>'
total = '<total>(.*?)</total>'
amount = '<amount>(.*?)</amount>'
number = '<number>(.*?)</number>'
cat_win_numbers = '<cat_win_numbers>(.*?)</cat_win_numbers>'
range_90 = ["01", "02", "03", "04", "05", "06", "07", "08", "09"] + [str(i) for i in range(10, 91)]
range_75 = ["01", "02", "03", "04", "05", "06", "07", "08", "09"] + [str(i) for i in range(10, 76)]
range_36 = ["01", "02", "03", "04", "05", "06", "07", "08", "09"] + [str(i) for i in range(10, 37)]

# -------------------------------------------------------------------------




class ResultAndPrizeHelper:

    def __init__(self, app):
        self.app = app


# ----- парсеры текста в отчётах:

    def parser_report_text_winners(self):
        wd = self.app.wd
        mskw = f"{datetime.today():%d/%m/%Y, %H:%M:%S МСК}"
        lokw = f"{datetime.today():%d/%m/%Y, %H:%M:%S ЛОК}"
        if len(wd.find_element_by_css_selector("div.report-item.report-item_winners").text) > 0:
            textwinners = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        assert "Продавец: 2000006810-20003511" in textwinners
        assert textwinners.find(mskw)
        assert textwinners.find(lokw)
        return textwinners



# --------------------------------------------------------------


# ------ клики по кнопкам:

    def button_get_report_winners(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()


    def open_page_results_and_prizes(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("span.icon.icon-results").click()


    def comeback_main_page(self):
        wd = self.app.wd
        # click comeback
        wd.find_element_by_css_selector("a.btn.btn_transperent").click()
        # click close modal window
        wd.find_element_by_css_selector("a.modal__body-close").click()


    def click_ok_in_winning_draw_numbers_modal_window(self):
        wd = self.app.wd
        for text_info_draw_window in wd.find_elements_by_css_selector("div.modal__body.modal__body_small"):
            text_draw = text_info_draw_window.text
        assert "Укажите тираж:" in text_draw
        wd.find_element_by_css_selector("button.btn.btn_transperent").click()


    def select_draw_10563_in_draw_numbers(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").clear()
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").send_keys("10563")


    def select_draw_130600_in_draw_numbers(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").clear()
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").send_keys("130600")


    def select_draw_9000_in_draw_numbers(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").clear()
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").send_keys("9000")


    def select_draw_30000_in_draw_numbers(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").clear()
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").send_keys("30000")


    def select_draw_2000_in_draw_numbers(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").clear()
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").send_keys("2000")


    def select_draw_2001_in_draw_numbers(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").clear()
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").send_keys("2001")


    def select_draw_1966_in_draw_numbers(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").clear()
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").send_keys("1966")


    def select_draw_1600_in_draw_numbers(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").clear()
        wd.find_element_by_css_selector("input.input-text.report__input-id.input-prompt").send_keys("1600")


    def click_ok_for_several_draws_modal_window(self):
        wd = self.app.wd
        for text_info_draw_window in wd.find_elements_by_css_selector("div.modal__body.modal__body_small"):
            text_draw = text_info_draw_window.text
        assert "Укажите интервал от указанного\nтиража и запрошенное количество перед ним:" in text_draw
        wd.find_element_by_css_selector("button.btn.btn_transperent").click()


    def click_ok_in_modal_window_current_date(self):
        wd = self.app.wd
        datetoday = f"{datetime.today():%d.%m.%Y}"
        datemodal = wd.find_element_by_css_selector(
            "div.react-datepicker__input-container > input").get_attribute('value')
        assert datetoday == datemodal
        wd.find_element_by_css_selector("button.btn.btn_transperent").click()


    def previous_month_day_10_modal_window(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.react-datepicker__input-container ").click()
        wd.find_element_by_css_selector(
            "a.react-datepicker__navigation.react-datepicker__navigation--previous").click()
        wd.find_element_by_xpath("(//div[@aria-label='day-10'])").click()


    def assert_previous_month_day_10_input_modal_window(self):
        wd = self.app.wd
        inputm = datetime.today()
        if inputm.month == 1:
            last_month_draw = f"{inputm.replace(month=12, day=10, year=inputm.year - 1):%d.%m.%Y}"
        else:
            last_month_draw = f"{inputm.replace(month=inputm.month - 1, day=10):%d.%m.%Y}"
        return last_month_draw


    def click_ok_in_modal_window(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("button.btn.btn_transperent").click()




# --------------------------------------------------------


# ------ клики по результатам тиражей:

    def click_winning_numbers_of_the_last_4_draws(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='date2']").click()


    def click_winning_draw_numbers(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='date6']").click()


    def click_the_winning_numbers_for_several_draws(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='date7']").click()


    def click_results_of_the_last_draw(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='date3']").click()


    def click_the_results_of_the_draw(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='date8']").click()


    def click_the_results_of_the_draw_date(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='date4']").click()


    def click_results_for_several_draws(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='date9']").click()


    def click_sum_superprize(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='date5']").click()


# ------------------------------------------------------------




# ------ клики по играм:

    def click_game_4x20(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='game_4420']").click()


    def click_game_5x36(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='game_5536']").click()


    def click_game_6x45(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='game_5101']").click()


    def click_game_7x49(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='game_5150']").click()


    def click_game_6x49(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='game_5219']").click()


    def click_game_matchball(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='game_5550']").click()


    def click_game_zodiac(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='game_28005']").click()


    def click_game_russianlotto(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='game_7103']").click()


    def click_game_housinglottery(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='game_7105']").click()


    def click_game_goldhorseshoe(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='game_7115']").click()


    def click_game_bingo75(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='game_7175']").click()


    def click_game_6x36(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='game_7101']").click()


    def click_game_rapido(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='game_5211']").click()


# ---------------------------------------------------------------


# ------------ отправка запросов в gate для игры 4на20:

    def message_id_33_4x20_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_4420, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        assert f"ЛОТО 4/20 - Тираж {d[0]} :" in text_win


    def message_id_33_4x20_winning_numbers_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_4420, auth=HTTPBasicAuth(*auth))
        response = response.text
        w = re.findall(win_numbers, response)
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
            else:
                assert w[0] in text_win


    def message_id_33_4x20_winning_numbers_4_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_2_4420, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"ЛОТО 4/20 - Тираж {d[0]} :" in text_win
        assert f"ЛОТО 4/20 - Тираж {d[1]} :" in text_win
        assert f"ЛОТО 4/20 - Тираж {d[2]} :" in text_win
        assert f"ЛОТО 4/20 - Тираж {d[3]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win


    def message_id_33_4x20_winning_numbers_for_5_draws(self):
        ws = []
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date7 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=7&GAME_ID=4420&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"ЛОТО 4/20 - Тираж {d[0]} :" in text_win
        assert f"ЛОТО 4/20 - Тираж {d[1]} :" in text_win
        assert f"ЛОТО 4/20 - Тираж {d[2]} :" in text_win
        assert f"ЛОТО 4/20 - Тираж {d[3]} :" in text_win
        assert f"ЛОТО 4/20 - Тираж {d[4]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win


    def message_id_33_4x20_results_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_3_4420, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        assert f"ЛОТО 4/20 - Тираж {d[0]} :" in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_4x20_results_draw_date_current_date(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_4_4420, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_4x20_results_draw_date_previous_date(self):
        wd = self.app.wd
        # делаем дату предыдущего месяца 10е число для запроса 33
        dd = datetime.today()
        if dd.month == 1:
            last_month = f"{dd.replace(month=12, day=10, year=dd.year - 1):%Y.%m.%d}"
        else:
            last_month = f"{dd.replace(month=dd.month - 1, day=10):%Y.%m.%d}"
        DATE_START_LAST_MONTH = f"{last_month}+03"
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&GAME_ID=4420&DATE_START="{DATE_START_LAST_MONTH}"&DRAW_ID=0&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_4x20_results_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date9 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=9&GAME_ID=4420&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_4x20_superprizes(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_5_4420, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        a = re.findall(amount, response)
        assert f"ЛОТО 4/20 - Тираж {d[0]} :" in text_win
        if len(a) == 0:
            assert "СУПЕРПРИЗА НЕТ" in text_win
        if len(a) == 1:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
        if len(a) == 2:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
            assert f"Приз\n{a[1]}" in text_win


# --------------------------------------------------------------------------


# ------------ отправка запросов в gate для игры 5из36:


    def message_id_33_5x36_results_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date9 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=9&GAME_ID=5536&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_5x36_results_draw_date_current_date(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_4_5536, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_5x36_results_draw_date_previous_date(self):
        wd = self.app.wd
        # делаем дату предыдущего месяца 10е число для запроса 33
        dd = datetime.today()
        if dd.month == 1:
            last_month = f"{dd.replace(month=12, day=10, year=dd.year - 1):%Y.%m.%d}"
        else:
            last_month = f"{dd.replace(month=dd.month - 1, day=10):%Y.%m.%d}"
        DATE_START_LAST_MONTH = f"{last_month}+03"
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&GAME_ID=5536&DATE_START="{DATE_START_LAST_MONTH}"&DRAW_ID=0&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_5x36_results_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_3_5536, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        assert f"ЛОТО 5/36 - Тираж {d[0]} :" in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_5x36_superprizes(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_5_5536, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        a = re.findall(amount, response)
        assert f"ЛОТО 5/36 - Тираж {d[0]} :" in text_win
        if len(a) == 0:
            assert "СУПЕРПРИЗА НЕТ" in text_win
        if len(a) == 1:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
        if len(a) == 2:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
            assert f"Приз\n{a[1]}" in text_win


    def message_id_33_5x36_winning_numbers_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date7 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=7&GAME_ID=5536&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"ЛОТО 5/36 - Тираж {d[0]} :" in text_win
        assert f"ЛОТО 5/36 - Тираж {d[1]} :" in text_win
        assert f"ЛОТО 5/36 - Тираж {d[2]} :" in text_win
        assert f"ЛОТО 5/36 - Тираж {d[3]} :" in text_win
        assert f"ЛОТО 5/36 - Тираж {d[4]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win


    def message_id_33_5x36_winning_numbers_4_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_2_5536, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"ЛОТО 5/36 - Тираж {d[0]} :" in text_win
        assert f"ЛОТО 5/36 - Тираж {d[1]} :" in text_win
        assert f"ЛОТО 5/36 - Тираж {d[2]} :" in text_win
        assert f"ЛОТО 5/36 - Тираж {d[3]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win


    def message_id_33_5x36_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_5536, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        assert f"ЛОТО 5/36 - Тираж {d[0]} :" in text_win


    def message_id_33_5x36_winning_numbers_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_5536, auth=HTTPBasicAuth(*auth))
        response = response.text
        w = re.findall(win_numbers, response)
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
            else:
                assert w[0] in text_win



# --------------------------------------------------------------------------


# ------------ отправка запросов в gate для игры 6из45:

    def message_id_33_6x45_results_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date9 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=9&GAME_ID=5101&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_6x45_results_draw_date_current_date(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_4_5101, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_6x45_results_draw_date_previous_date(self):
        wd = self.app.wd
        # делаем дату предыдущего месяца 10е число для запроса 33
        dd = datetime.today()
        if dd.month == 1:
            last_month = f"{dd.replace(month=12, day=10, year=dd.year - 1):%Y.%m.%d}"
        else:
            last_month = f"{dd.replace(month=dd.month - 1, day=10):%Y.%m.%d}"
        DATE_START_LAST_MONTH = f"{last_month}+03"
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&GAME_ID=5101&DATE_START="{DATE_START_LAST_MONTH}"&DRAW_ID=0&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_6x45_results_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_3_5101, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        assert f"ЛОТО 6/45 - Тираж {d[0]} :" in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_6x45_superprizes(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_5_5101, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        a = re.findall(amount, response)
        assert f"ЛОТО 6/45 - Тираж {d[0]} :" in text_win
        if len(a) == 0:
            assert "СУПЕРПРИЗА НЕТ" in text_win
        if len(a) == 1:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
        if len(a) == 2:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
            assert f"Приз\n{a[1]}" in text_win


    def message_id_33_6x45_winning_numbers_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date7 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=7&GAME_ID=5101&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"ЛОТО 6/45 - Тираж {d[0]} :" in text_win
        assert f"ЛОТО 6/45 - Тираж {d[1]} :" in text_win
        assert f"ЛОТО 6/45 - Тираж {d[2]} :" in text_win
        assert f"ЛОТО 6/45 - Тираж {d[3]} :" in text_win
        assert f"ЛОТО 6/45 - Тираж {d[4]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win



    def message_id_33_6x45_winning_numbers_4_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_2_5101, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"ЛОТО 6/45 - Тираж {d[0]} :" in text_win
        assert f"ЛОТО 6/45 - Тираж {d[1]} :" in text_win
        assert f"ЛОТО 6/45 - Тираж {d[2]} :" in text_win
        assert f"ЛОТО 6/45 - Тираж {d[3]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win


    def message_id_33_6x45_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_5101, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        assert f"ЛОТО 6/45 - Тираж {d[0]} :" in text_win



    def message_id_33_6x45_winning_numbers_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_5101, auth=HTTPBasicAuth(*auth))
        response = response.text
        w = re.findall(win_numbers, response)
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
            else:
                assert w[0] in text_win





# --------------------------------------------------------------------------


# ------------ отправка запросов в gate для игры 7из49:

    def message_id_33_7x49_results_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date9 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=9&GAME_ID=5150&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_7x49_results_draw_date_current_date(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_4_5150, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_7x49_results_draw_date_previous_date(self):
        wd = self.app.wd
        # делаем дату предыдущего месяца 10е число для запроса 33
        dd = datetime.today()
        if dd.month == 1:
            last_month = f"{dd.replace(month=12, day=10, year=dd.year - 1):%Y.%m.%d}"
        else:
            last_month = f"{dd.replace(month=dd.month - 1, day=10):%Y.%m.%d}"
        DATE_START_LAST_MONTH = f"{last_month}+03"
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&GAME_ID=5150&DATE_START="{DATE_START_LAST_MONTH}"&DRAW_ID=0&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_7x49_results_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_3_5150, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        assert f"ЛОТО 7/49 - Тираж {d[0]} :" in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_7x49_superprizes(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_5_5150, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        a = re.findall(amount, response)
        assert f"ЛОТО 7/49 - Тираж {d[0]} :" in text_win
        if len(a) == 0:
            assert "СУПЕРПРИЗА НЕТ" in text_win
        if len(a) == 1:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
        if len(a) == 2:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
            assert f"Приз\n{a[1]}" in text_win


    def message_id_33_7x49_winning_numbers_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date7 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=7&GAME_ID=5150&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"ЛОТО 7/49 - Тираж {d[0]} :" in text_win
        assert f"ЛОТО 7/49 - Тираж {d[1]} :" in text_win
        assert f"ЛОТО 7/49 - Тираж {d[2]} :" in text_win
        assert f"ЛОТО 7/49 - Тираж {d[3]} :" in text_win
        assert f"ЛОТО 7/49 - Тираж {d[4]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win


    def message_id_33_7x49_winning_numbers_4_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_2_5150, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"ЛОТО 7/49 - Тираж {d[0]} :" in text_win
        assert f"ЛОТО 7/49 - Тираж {d[1]} :" in text_win
        assert f"ЛОТО 7/49 - Тираж {d[2]} :" in text_win
        assert f"ЛОТО 7/49 - Тираж {d[3]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win


    def message_id_33_7x49_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_5150, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        assert f"ЛОТО 7/49 - Тираж {d[0]} :" in text_win


    def message_id_33_7x49_winning_numbers_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_5150, auth=HTTPBasicAuth(*auth))
        response = response.text
        w = re.findall(win_numbers, response)
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
            else:
                assert w[0] in text_win



# --------------------------------------------------------------------------


# ------------ отправка запросов в gate для игры матчбол:

    def message_id_33_matchball_results_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date9 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=9&GAME_ID=5550&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_matchball_results_draw_date_current_date(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_4_5550, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_matchball_results_draw_date_previous_date(self):
        wd = self.app.wd
        # делаем дату предыдущего месяца 10е число для запроса 33
        dd = datetime.today()
        if dd.month == 1:
            last_month = f"{dd.replace(month=12, day=10, year=dd.year - 1):%Y.%m.%d}"
        else:
            last_month = f"{dd.replace(month=dd.month - 1, day=10):%Y.%m.%d}"
        DATE_START_LAST_MONTH = f"{last_month}+03"
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&GAME_ID=5550&DATE_START="{DATE_START_LAST_MONTH}"&DRAW_ID=0&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_matchball_results_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_3_5550, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        assert f"МАТЧБОЛ - Тираж {d[0]} :" in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_matchball_superprizes(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_5_5550, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        a = re.findall(amount, response)
        assert f"МАТЧБОЛ - Тираж {d[0]} :" in text_win
        if len(a) == 0:
            assert "СУПЕРПРИЗА НЕТ" in text_win
        if len(a) == 1:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
        if len(a) == 2:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
            assert f"Приз\n{a[1]}" in text_win


    def message_id_33_matchball_winning_numbers_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date7 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=7&GAME_ID=5550&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"МАТЧБОЛ - Тираж {d[0]} :" in text_win
        assert f"МАТЧБОЛ - Тираж {d[1]} :" in text_win
        assert f"МАТЧБОЛ - Тираж {d[2]} :" in text_win
        assert f"МАТЧБОЛ - Тираж {d[3]} :" in text_win
        assert f"МАТЧБОЛ - Тираж {d[4]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win


    def message_id_33_matchball_winning_numbers_4_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_2_5550, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"МАТЧБОЛ - Тираж {d[0]} :" in text_win
        assert f"МАТЧБОЛ - Тираж {d[1]} :" in text_win
        assert f"МАТЧБОЛ - Тираж {d[2]} :" in text_win
        assert f"МАТЧБОЛ - Тираж {d[3]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win


    def message_id_33_matchball_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_5550, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        assert f"МАТЧБОЛ - Тираж {d[0]} :" in text_win


    def message_id_33_matchball_winning_numbers_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_5550, auth=HTTPBasicAuth(*auth))
        response = response.text
        w = re.findall(win_numbers, response)
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
            else:
                assert w[0] in text_win




# --------------------------------------------------------------------------

# ------------ отправка запросов в gate для игры зодиак:

    def message_id_33_zodiac_results_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date9 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=9&GAME_ID=28005&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_zodiac_results_draw_date_current_date(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_4_28005, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_zodiac_results_draw_date_previous_date(self):
        wd = self.app.wd
        # делаем дату предыдущего месяца 10е число для запроса 33
        dd = datetime.today()
        if dd.month == 1:
            last_month = f"{dd.replace(month=12, day=10, year=dd.year - 1):%Y.%m.%d}"
        else:
            last_month = f"{dd.replace(month=dd.month - 1, day=10):%Y.%m.%d}"
        DATE_START_LAST_MONTH = f"{last_month}+03"
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&GAME_ID=28005&DATE_START="{DATE_START_LAST_MONTH}"&DRAW_ID=0&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_zodiac_results_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_3_28005, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        assert f"Зодиак - Тираж {d[0]} :" in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_zodiac_superprizes(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_5_28005, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        a = re.findall(amount, response)
        assert f"Зодиак - Тираж {d[0]} :" in text_win
        if len(a) == 0:
            assert "СУПЕРПРИЗА НЕТ" in text_win
        if len(a) == 1:
            assert f"Суперприз\n{a[0]}" in text_win
            assert "Категория\nСумма руб." in text_win
        if len(a) == 2:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
            assert f"Приз\n{a[1]}" in text_win


    def message_id_33_zodiac_winning_numbers_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date7 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=7&GAME_ID=28005&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"Зодиак - Тираж {d[0]} :" in text_win
        assert f"Зодиак - Тираж {d[1]} :" in text_win
        assert f"Зодиак - Тираж {d[2]} :" in text_win
        assert f"Зодиак - Тираж {d[3]} :" in text_win
        assert f"Зодиак - Тираж {d[4]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win


    def message_id_33_zodiac_winning_numbers_4_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_2_28005, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"Зодиак - Тираж {d[0]} :" in text_win
        assert f"Зодиак - Тираж {d[1]} :" in text_win
        assert f"Зодиак - Тираж {d[2]} :" in text_win
        assert f"Зодиак - Тираж {d[3]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win


    def message_id_33_zodiac_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_28005, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        assert f"Зодиак - Тираж {d[0]} :" in text_win


    def message_id_33_zodiac_winning_numbers_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_28005, auth=HTTPBasicAuth(*auth))
        response = response.text
        w = re.findall(win_numbers, response)
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
            else:
                assert w[0] in text_win




# --------------------------------------------------------------------------


# ------------ отправка запросов в gate для игры Русское лото:

    def message_id_33_russianlotto_results_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date9 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=9&GAME_ID=7103&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"РУССКОЕ ЛОТО - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_russianlotto_results_draw_date_current_date(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_4_7103, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"РУССКОЕ ЛОТО - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_russianlotto_results_draw_date_previous_date(self):
        wd = self.app.wd
        # делаем дату предыдущего месяца 10е число для запроса 33
        dd = datetime.today()
        if dd.month == 1:
            last_month = f"{dd.replace(month=12, day=10, year=dd.year - 1):%Y.%m.%d}"
        else:
            last_month = f"{dd.replace(month=dd.month - 1, day=10):%Y.%m.%d}"
        DATE_START_LAST_MONTH = f"{last_month}+03"
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&GAME_ID=7103&DATE_START="{DATE_START_LAST_MONTH}"&DRAW_ID=0&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"РУССКОЕ ЛОТО - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_russianlotto_results_draw_2000(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date8 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=8&GAME_ID=7103&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=0&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"РУССКОЕ ЛОТО - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_russianlotto_results_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_3_7103, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"РУССКОЕ ЛОТО - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_russianlotto_superprizes(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_5_7103, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        a = re.findall(amount, response)
        assert f"РУССКОЕ ЛОТО - Тираж {d[0]} :" in text_win
        if len(a) == 0:
            assert "СУПЕРПРИЗА НЕТ" in text_win
        if len(a) == 1:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
        if len(a) == 2:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
            assert f"Приз\n{a[1]}" in text_win


    def message_id_33_russianlotto_winning_numbers_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date7 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=7&GAME_ID=7103&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        missing_numbers = []
        assert f"РУССКОЕ ЛОТО - Тираж {d[0]} :" in text_win
        assert f"РУССКОЕ ЛОТО - Тираж {d[1]} :" in text_win
        assert f"РУССКОЕ ЛОТО - Тираж {d[2]} :" in text_win
        assert f"РУССКОЕ ЛОТО - Тираж {d[3]} :" in text_win
        assert f"РУССКОЕ ЛОТО - Тираж {d[4]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
        ws = wn
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win
        # Невыпавшие числа алгоритм:
        for sp in ws[:]:
            for i in range_90:
                if str(i) not in sp:
                    missing_numbers.append(i)
            assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


    def message_id_33_russianlotto_winning_draw_numbers_2000(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date6 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=6&GAME_ID=7103&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=0&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        missing_numbers = []
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        for i in d:
            assert f"РУССКОЕ ЛОТО - Тираж {i}" in text_win
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
            else:
                assert wn[0] in text_win
                # Невыпавшие числа алгоритм:
                for sp in wn[:]:
                    for i in range_90:
                        if str(i) not in sp:
                            missing_numbers.append(i)
                    assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


    def message_id_33_russianlotto_winning_numbers_4_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_2_7103, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        missing_numbers = []
        assert f"РУССКОЕ ЛОТО - Тираж {d[0]} :" in text_win
        assert f"РУССКОЕ ЛОТО - Тираж {d[1]} :" in text_win
        assert f"РУССКОЕ ЛОТО - Тираж {d[2]} :" in text_win
        assert f"РУССКОЕ ЛОТО - Тираж {d[3]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
        ws = wn
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win
        # Невыпавшие числа алгоритм:
        for sp in ws[:]:
            for i in range_90:
                if str(i) not in sp:
                    missing_numbers.append(i)
            assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


    def message_id_33_russianlotto_winning_numbers_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_7103, auth=HTTPBasicAuth(*auth))
        response = response.text
        missing_numbers = []
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        for i in d:
            assert f"РУССКОЕ ЛОТО - Тираж {i}" in text_win
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
            else:
                assert wn[0] in text_win
                # Невыпавшие числа алгоритм:
                for sp in wn[:]:
                    for i in range_75:
                        if str(i) not in sp:
                            missing_numbers.append(i)
                    assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


# --------------------------------------------------------------------------


# ------------ отправка запросов в gate для игры Жилищная лотерея:

    def message_id_33_housinglottery_results_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date9 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=9&GAME_ID=7105&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"ЖЛ - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_housinglottery_results_draw_date_current_date(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_4_7105, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"ЖЛ - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_housinglottery_results_draw_date_previous_date(self):
        wd = self.app.wd
        # делаем дату предыдущего месяца 10е число для запроса 33
        dd = datetime.today()
        if dd.month == 1:
            last_month = f"{dd.replace(month=12, day=10, year=dd.year - 1):%Y.%m.%d}"
        else:
            last_month = f"{dd.replace(month=dd.month - 1, day=10):%Y.%m.%d}"
        DATE_START_LAST_MONTH = f"{last_month}+03"
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&GAME_ID=7105&DATE_START="{DATE_START_LAST_MONTH}"&DRAW_ID=0&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"ЖЛ - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_housinglottery_results_draw_2000(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date8 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=8&GAME_ID=7105&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=0&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"ЖЛ - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_housinglottery_results_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_3_7105, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"ЖЛ - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_housinglottery_superprizes(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_5_7105, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        a = re.findall(amount, response)
        assert f"ЖЛ - Тираж {d[0]} :" in text_win
        if len(a) == 0:
            assert "СУПЕРПРИЗА НЕТ" in text_win
        if len(a) == 1:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
        if len(a) == 2:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
            assert f"Приз\n{a[1]}" in text_win


    def message_id_33_housinglottery_winning_draw_numbers_2000(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date6 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=6&GAME_ID=7105&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=0&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        missing_numbers = []
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        for i in d:
            assert f"ЖЛ - Тираж {i}" in text_win
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
            else:
                assert wn[0] in text_win
                # Невыпавшие числа алгоритм:
                for sp in wn[:]:
                    for i in range_90:
                        if str(i) not in sp:
                            missing_numbers.append(i)
                    assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


    def message_id_33_housinglottery_winning_numbers_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date7 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=7&GAME_ID=7105&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        missing_numbers = []
        assert f"ЖЛ - Тираж {d[0]} :" in text_win
        assert f"ЖЛ - Тираж {d[1]} :" in text_win
        assert f"ЖЛ - Тираж {d[2]} :" in text_win
        assert f"ЖЛ - Тираж {d[3]} :" in text_win
        assert f"ЖЛ - Тираж {d[4]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
        ws = wn
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win
        # Невыпавшие числа алгоритм:
        for sp in ws[:]:
            for i in range_90:
                if str(i) not in sp:
                    missing_numbers.append(i)
            assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


    def message_id_33_housinglottery_winning_numbers_4_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_2_7105, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        missing_numbers = []
        assert f"ЖЛ - Тираж {d[0]} :" in text_win
        assert f"ЖЛ - Тираж {d[1]} :" in text_win
        assert f"ЖЛ - Тираж {d[2]} :" in text_win
        assert f"ЖЛ - Тираж {d[3]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
        ws = wn
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win
        # Невыпавшие числа алгоритм:
        for sp in ws[:]:
            for i in range_90:
                if str(i) not in sp:
                    missing_numbers.append(i)
            assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


    def message_id_33_housinglottery_winning_numbers_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_7105, auth=HTTPBasicAuth(*auth))
        response = response.text
        missing_numbers = []
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        for i in d:
            assert f"ЖЛ - Тираж {i}" in text_win
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
            else:
                assert wn[0] in text_win
                # Невыпавшие числа алгоритм:
                for sp in wn[:]:
                    for i in range_75:
                        if str(i) not in sp:
                            missing_numbers.append(i)
                    assert f"Невыпавшие числа:\n{missing_numbers}" in text_win





# --------------------------------------------------------------------------


# ------------ отправка запросов в gate для игры Золотая подкова:

    def message_id_33_goldhorseshoe_results_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date9 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=9&GAME_ID=7115&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_goldhorseshoe_results_draw_date_current_date(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_4_7115, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_goldhorseshoe_results_draw_date_previous_date(self):
        wd = self.app.wd
        # делаем дату предыдущего месяца 10е число для запроса 33
        dd = datetime.today()
        if dd.month == 1:
            last_month = f"{dd.replace(month=12, day=10, year=dd.year - 1):%Y.%m.%d}"
        else:
            last_month = f"{dd.replace(month=dd.month - 1, day=10):%Y.%m.%d}"
        DATE_START_LAST_MONTH = f"{last_month}+03"
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&GAME_ID=7115&DATE_START="{DATE_START_LAST_MONTH}"&DRAW_ID=0&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_goldhorseshoe_results_draw_1600(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date8 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=8&GAME_ID=7115&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=0&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_goldhorseshoe_results_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_3_7115, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_goldhorseshoe_superprizes(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_5_7115, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        a = re.findall(amount, response)
        assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {d[0]} :" in text_win
        if len(a) == 0:
            assert "СУПЕРПРИЗА НЕТ" in text_win
        if len(a) == 1:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
        if len(a) == 2:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
            assert f"Приз\n{a[1]}" in text_win


    def message_id_33_goldhorseshoe_winning_draw_numbers_1600(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date6 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=6&GAME_ID=7115&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=0&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        missing_numbers = []
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        for i in d:
            assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {i}" in text_win
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
            else:
                assert wn[0] in text_win
                # Невыпавшие числа алгоритм:
                for sp in wn[:]:
                    for i in range_90:
                        if str(i) not in sp:
                            missing_numbers.append(i)
                    assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


    def message_id_33_goldhorseshoe_winning_numbers_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date7 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=7&GAME_ID=7115&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        missing_numbers = []
        assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {d[0]} :" in text_win
        assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {d[1]} :" in text_win
        assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {d[2]} :" in text_win
        assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {d[3]} :" in text_win
        assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {d[4]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
        ws = wn
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win
        # Невыпавшие числа алгоритм:
        for sp in ws[:]:
            for i in range_90:
                if str(i) not in sp:
                    missing_numbers.append(i)
            assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


    def message_id_33_goldhorseshoe_winning_numbers_4_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_2_7115, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        missing_numbers = []
        assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {d[0]} :" in text_win
        assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {d[1]} :" in text_win
        assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {d[2]} :" in text_win
        assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {d[3]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
        ws = wn
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win
        # Невыпавшие числа алгоритм:
        for sp in ws[:]:
            for i in range_90:
                if str(i) not in sp:
                    missing_numbers.append(i)
            assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


    def message_id_33_goldhorseshoe_winning_numbers_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_7115, auth=HTTPBasicAuth(*auth))
        response = response.text
        missing_numbers = []
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        for i in d:
            assert f"ЗОЛОТАЯ ПОДКОВА - Тираж {i}" in text_win
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
            else:
                assert wn[0] in text_win
                # Невыпавшие числа алгоритм:
                for sp in wn[:]:
                    for i in range_75:
                        if str(i) not in sp:
                            missing_numbers.append(i)
                    assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


# --------------------------------------------------------------------------


# ------------ отправка запросов в gate для игры Бинго 75:

    def message_id_33_bingo75_results_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date9 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=9&GAME_ID=7175&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"Бинго-75 - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_bingo75_results_draw_date_current_date(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_4_7175, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"Бинго-75 - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_bingo75_results_draw_date_previous_date(self):
        wd = self.app.wd
        # делаем дату предыдущего месяца 10е число для запроса 33
        dd = datetime.today()
        if dd.month == 1:
            last_month = f"{dd.replace(month=12, day=10, year=dd.year - 1):%Y.%m.%d}"
        else:
            last_month = f"{dd.replace(month=dd.month - 1, day=10):%Y.%m.%d}"
        DATE_START_LAST_MONTH = f"{last_month}+03"
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&GAME_ID=7175&DATE_START="{DATE_START_LAST_MONTH}"&DRAW_ID=0&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"Бинго-75 - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_bingo75_results_draw_2000(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date8 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=8&GAME_ID=7175&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=0&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"Бинго-75 - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_bingo75_results_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_3_7175, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"Бинго-75 - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_bingo75_superprizes(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_5_7175, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        a = re.findall(amount, response)
        assert f"Бинго-75 - Тираж {d[0]} :" in text_win
        if len(a) == 0:
            assert "СУПЕРПРИЗА НЕТ" in text_win
        if len(a) == 1:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
        if len(a) == 2:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
            assert f"Приз\n{a[1]}" in text_win


    def message_id_33_bingo75_winning_draw_numbers_2001(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date6 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=6&GAME_ID=7175&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=0&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        a = []
        b = ''
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        for i in d:
            assert f"Бинго-75 - Тираж {i}" in text_win
        for i in wn:
            assert i in text_win
        # Невыпавшие числа алгоритм
        for x in range_75:
            for y in wn:
                if x not in y:
                    a.append(x)
                    b = " ".join(a)
        assert f"Невыпавшие числа:\n{b}" in text_win


    def message_id_33_bingo75_winning_numbers_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date7 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=7&GAME_ID=7175&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        missing_numbers = []
        assert f"Бинго-75 - Тираж {d[0]} :" in text_win
        assert f"Бинго-75 - Тираж {d[1]} :" in text_win
        assert f"Бинго-75 - Тираж {d[2]} :" in text_win
        assert f"Бинго-75 - Тираж {d[3]} :" in text_win
        assert f"Бинго-75 - Тираж {d[4]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
        ws = wn
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win
        # Невыпавшие числа алгоритм:
        for sp in ws[:]:
            for i in range_75:
                if str(i) not in sp:
                    missing_numbers.append(i)
            assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


    def message_id_33_bingo75_winning_numbers_4_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_2_7175, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        missing_numbers = []
        assert f"Бинго-75 - Тираж {d[0]} :" in text_win
        assert f"Бинго-75 - Тираж {d[1]} :" in text_win
        assert f"Бинго-75 - Тираж {d[2]} :" in text_win
        assert f"Бинго-75 - Тираж {d[3]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
        ws = wn
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win
        # Невыпавшие числа алгоритм:
        for sp in ws[:]:
            for i in range_75:
                if str(i) not in sp:
                    missing_numbers.append(i)
            assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


    def message_id_33_bingo75_winning_numbers_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_7175, auth=HTTPBasicAuth(*auth))
        response = response.text
        missing_numbers = []
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        for i in d:
            assert f"Бинго-75 - Тираж {i}" in text_win
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
            else:
                assert wn[0] in text_win
                # Невыпавшие числа алгоритм:
                for sp in wn[:]:
                    for i in range_75:
                        if str(i) not in sp:
                            missing_numbers.append(i)
                    assert f"Невыпавшие числа:\n{missing_numbers}" in text_win








# --------------------------------------------------------------------------


# ------------ отправка запросов в gate для игры 6 из 36:

    def message_id_33_6x36_results_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date9 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=9&GAME_ID=7101&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"6/36 - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_6x36_results_draw_date_current_date(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_4_7101, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"6/36 - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_6x36_results_draw_date_previous_date(self):
        wd = self.app.wd
        # делаем дату предыдущего месяца 10е число для запроса 33
        dd = datetime.today()
        if dd.month == 1:
            last_month = f"{dd.replace(month=12, day=10, year=dd.year - 1):%Y.%m.%d}"
        else:
            last_month = f"{dd.replace(month=dd.month - 1, day=10):%Y.%m.%d}"
        DATE_START_LAST_MONTH = f"{last_month}+03"
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&GAME_ID=7101&DATE_START="{DATE_START_LAST_MONTH}"&DRAW_ID=0&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"6/36 - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_6x36_results_draw_1600(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date8 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=8&GAME_ID=7101&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=0&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"6/36 - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_6x36_results_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_3_7101, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        n = re.findall(number, response)
        cwn = re.findall(cat_win_numbers, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert f"6/36 - Тираж {i}" in text_win
        for i in n:
            assert f"Тур: {i}" in text_win
        for i in cwn:
            assert f"Выпавшие числа: {i}" in text_win
        for i in wc:
            assert f"Выигрывших билетов: {i}" in text_win
        for i in wa:
            assert f"Сумма выигрыша: {i}" in text_win
        for i in t:
            assert f"Общая сумма: {i}" in text_win


    def message_id_33_6x36_superprizes(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_5_7101, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        a = re.findall(amount, response)
        assert f"6/36 - Тираж {d[0]} :" in text_win
        if len(a) == 0:
            assert "СУПЕРПРИЗА НЕТ" in text_win
        if len(a) == 1:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
        if len(a) == 2:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
            assert f"Приз\n{a[1]}" in text_win


    def message_id_33_6x36_winning_draw_numbers_1600(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date6 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=6&GAME_ID=7101&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=0&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        a = []
        b = ''
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        for i in d:
            assert f"6/36 - Тираж {i}" in text_win
        for i in wn:
            assert i in text_win
        # Невыпавшие числа алгоритм
        for x in range_36:
            for y in wn:
                if x not in y:
                    a.append(x)
                    b = " ".join(a)
        assert f"Невыпавшие числа:\n{b}" in text_win


    def message_id_33_6x36_winning_numbers_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date7 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=7&GAME_ID=7101&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        missing_numbers = []
        assert f"6/36 - Тираж {d[0]} :" in text_win
        assert f"6/36 - Тираж {d[1]} :" in text_win
        assert f"6/36 - Тираж {d[2]} :" in text_win
        assert f"6/36 - Тираж {d[3]} :" in text_win
        assert f"6/36 - Тираж {d[4]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
        ws = wn
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win
        # Невыпавшие числа алгоритм:
        for sp in ws[:]:
            for i in range_36:
                if str(i) not in sp:
                    missing_numbers.append(i)
            assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


    def message_id_33_6x36_winning_numbers_4_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_2_7101, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        missing_numbers = []
        assert f"6/36 - Тираж {d[0]} :" in text_win
        assert f"6/36 - Тираж {d[1]} :" in text_win
        assert f"6/36 - Тираж {d[2]} :" in text_win
        assert f"6/36 - Тираж {d[3]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
        ws = wn
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win
        # Невыпавшие числа алгоритм:
        for sp in ws[:]:
            for i in range_36:
                if str(i) not in sp:
                    missing_numbers.append(i)
            assert f"Невыпавшие числа:\n{missing_numbers}" in text_win


    def message_id_33_6x36_winning_numbers_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_7101, auth=HTTPBasicAuth(*auth))
        response = response.text
        missing_numbers = []
        d = re.findall(draw_id, response)
        wn = re.findall(win_numbers, response)
        for i in d:
            assert f"6/36 - Тираж {i}" in text_win
        for s in wn[:]:
            if '""' in wn:
                wn.remove(s)
            else:
                assert wn[0] in text_win
                # Невыпавшие числа алгоритм:
                for sp in wn[:]:
                    for i in range_36:
                        if str(i) not in sp:
                            missing_numbers.append(i)
                    assert f"Невыпавшие числа:\n{missing_numbers}" in text_win




# --------------------------------------------------------------------------


# ------------ отправка запросов в gate для игры рапидо:

    def message_id_33_rapido_results_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date9 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=9&GAME_ID=5211&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_rapido_results_draw_date_current_date(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_4_5211, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_rapido_results_draw_date_previous_date(self):
        wd = self.app.wd
        # делаем дату предыдущего месяца 10е число для запроса 33
        dd = datetime.today()
        if dd.month == 1:
            last_month = f"{dd.replace(month=12, day=10, year=dd.year - 1):%Y.%m.%d}"
        else:
            last_month = f"{dd.replace(month=dd.month - 1, day=10):%Y.%m.%d}"
        DATE_START_LAST_MONTH = f"{last_month}+03"
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&GAME_ID=5211&DATE_START="{DATE_START_LAST_MONTH}"&DRAW_ID=0&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        for i in d:
            assert i in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_rapido_results_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_3_5211, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        wc = re.findall(winners_count, response)
        wa = re.findall(winning_amount, response)
        t = re.findall(total, response)
        assert f"РАПИДО - Тираж {d[0]} :" in text_win
        for i in wc:
            assert i in text_win
        for i in wa:
            assert i in text_win
        for i in t:
            assert i in text_win


    def message_id_33_rapido_superprizes(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_5_5211, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        a = re.findall(amount, response)
        assert f"РАПИДО - Тираж {d[0]} :" in text_win
        if len(a) == 0:
            assert "СУПЕРПРИЗА НЕТ" in text_win
        if len(a) == 1:
            assert f"Суперприз\n{a[0]}" in text_win
            assert "Категория\nСумма руб." in text_win
        if len(a) == 2:
            assert "Категория\nСумма руб." in text_win
            assert f"Суперприз\n{a[0]}" in text_win
            assert f"Приз\n{a[1]}" in text_win


    def message_id_33_rapido_winning_numbers_for_5_draws(self):
        wd = self.app.wd
        # draw = берём текст - это тираж с кнопки выигрышные номера нескольких тиражей
        draw = wd.find_element_by_css_selector("#date7 + .winners-reports__label .winners-reports__label-text").text
        drawi = int(draw)
        # Нажимаем кнопку получить отчёт в результатах и призах
        wd.find_element_by_css_selector("button.btn.btn_save.winners-button").click()
        # массив текста после нажатия на получить отчёт
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        # отправка запроса 33 для получения 5 тиражей послдних
        response = post(url=MessageID.URL_33,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=7&GAME_ID=5211&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"РАПИДО - Тираж {d[0]} :" in text_win
        assert f"РАПИДО - Тираж {d[1]} :" in text_win
        assert f"РАПИДО - Тираж {d[2]} :" in text_win
        assert f"РАПИДО - Тираж {d[3]} :" in text_win
        assert f"РАПИДО - Тираж {d[4]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win


    def message_id_33_rapido_winning_numbers_4_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_2_5211, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"РАПИДО - Тираж {d[0]} :" in text_win
        assert f"РАПИДО - Тираж {d[1]} :" in text_win
        assert f"РАПИДО - Тираж {d[2]} :" in text_win
        assert f"РАПИДО - Тираж {d[3]} :" in text_win
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
        ws = w
        for ss in ws[:]:
            assert ss in ws
            assert ss in text_win


    def message_id_33_rapido_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_5211, auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        assert f"РАПИДО - Тираж {d[0]} :" in text_win


    def message_id_33_rapido_winning_numbers_last_draw(self):
        wd = self.app.wd
        text_win = wd.find_element_by_css_selector("div.report-item.report-item_winners").text
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_5211, auth=HTTPBasicAuth(*auth))
        response = response.text
        w = re.findall(win_numbers, response)
        # Проверка: Если в  w(win_numbers) прилетает '""' ,
        # то удаляю строку так-как на экране больше не отображается '""'
        for s in w[:]:
            if '""' in w:
                w.remove(s)
            else:
                assert w[0] in text_win






# --------------------------------------------------------------------------