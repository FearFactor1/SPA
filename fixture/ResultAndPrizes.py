from datetime import datetime, timedelta
from requests import post
from requests.auth import HTTPBasicAuth
from fixture.messages import MessageID
import re



# ----------- Глобальные переменные:

login = "s3_http_access"
password = "ambush!Tidy4"
auth = (login, password)
draw_id = '<draw_id>(.*?)</draw_id>'
win_numbers = '<win_numbers>(.*?)</win_numbers>'
winners_count = '<winners_count>(.*?)</winners_count>'
winning_amount = '<winning_amount>(.*?)</winning_amount>'
total = '<total>(.*?)</total>'
amount = '<amount>(.*?)</amount>'

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


# ---------------------------------------------------------------


# ------------ отправки запросов в gate:

    def message_id_33_4x20_last_draw(self):
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_4420, auth=HTTPBasicAuth(*auth))
        response = response.text.split('\n')
        for row in response:
            if 'draw_id' in row:
                draw = row.replace('<draw_id>', '').replace('</draw_id>', '').strip()
                draw_r = f"ЛОТО 4/20 - Тираж {draw} :"
                print(draw_r)
        return draw_r


    def message_id_33_4x20_winning_numbers_last_draw(self):
        response = post(url=MessageID.URL_33, data=MessageID.DATA_33_REPORT_TYPE_1_4420, auth=HTTPBasicAuth(*auth))
        response = response.text.split('\n')
        for row in response:
            if 'win_numbers' in row:
                win = row.replace('<win_numbers>', '').replace('</win_numbers>', '').strip()
                print(win)
        return win


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
        assert w[0] in text_win
        assert w[1] in text_win
        assert w[2] in text_win
        assert w[3] in text_win


    def message_id_33_4x20_winning_numbers_for_5_draws(self):
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
                        data=f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=7&GAME_ID=4420&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        d = re.findall(draw_id, response)
        w = re.findall(win_numbers, response)
        assert f"ЛОТО 4/20 - Тираж {d[0]} :" in text_win
        assert f"ЛОТО 4/20 - Тираж {d[1]} :" in text_win
        assert f"ЛОТО 4/20 - Тираж {d[2]} :" in text_win
        assert f"ЛОТО 4/20 - Тираж {d[3]} :" in text_win
        assert f"ЛОТО 4/20 - Тираж {d[4]} :" in text_win
        assert w[0] in text_win
        assert w[1] in text_win
        assert w[2] in text_win
        assert w[3] in text_win
        assert w[4] in text_win


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
                        data=f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=4&GAME_ID=4420&DATE_START="{DATE_START_LAST_MONTH}"&DRAW_ID=0&DRAWS_NUMBER=5&VERSION=1',
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
                        data=f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=9&GAME_ID=4420&DATE_START="{MessageID.DATE_START}"&DRAW_ID={str(drawi)}&DRAWS_NUMBER=5&VERSION=1',
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
        assert "Категория\nСумма руб." in text_win
        if len(a) == 0:
            assert "СУПЕРПРИЗА НЕТ" in text_win
        if len(a) == 1:
            assert f"Суперприз\n{a[0]}" in text_win
        if len(a) == 2:
            assert f"Суперприз {a[0]}" in text_win
            assert f"Приз \n{a[1]}" in text_win





# --------------------------------------------------------------------------