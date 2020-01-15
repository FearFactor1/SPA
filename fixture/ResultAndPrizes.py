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


    def click_ok_in_winning_numbers_for_several_draws_modal_window(self):
        wd = self.app.wd
        for text_info_draw_window in wd.find_elements_by_css_selector("div.modal__body.modal__body_small"):
            text_draw = text_info_draw_window.text
        assert "Укажите интервал от указанного\nтиража и запрошенное количество перед ним:" in text_draw
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


# ------------------------------------------------------------




# ------ клики по играм:



# ---------------------------------------------------------------