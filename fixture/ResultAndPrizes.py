from datetime import datetime, timedelta




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



# ---------------------------------------------------------------