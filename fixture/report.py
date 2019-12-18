from datetime import datetime, timedelta
import calendar




class ReportHelper:

    def __init__(self, app):
        self.app = app

# ----- парсеры текста в отчётах:

    def parser_report_text(self):
        wd = self.app.wd
        msk = f"{datetime.today():%d/%m/%Y %H:%M:%S МСК}"
        lok = f"{datetime.today():%d/%m/%Y %H:%M:%S МСК (ЛОК)}"
        if len(wd.find_element_by_css_selector("div.report-item").text) > 0:
            test = wd.find_element_by_css_selector("div.report-item").text
            spl = test.split('\n')
        else:
            print("Пустой тег в отчёте")
        # print(' | '.join(spl))
        assert test.find(msk)
        assert test.find(lok)
        return test


    def parser_full_report_text(self):
        wd = self.app.wd
        mskf = f"{datetime.today():%d/%m/%Y %H:%M:%S МСК}"
        lokf = f"{datetime.today():%d/%m/%Y %H:%M:%S МСК (ЛОК)}"
        if len(wd.find_element_by_css_selector("div.report-item").text) > 0:
            textfull = wd.find_element_by_css_selector("div.report-item").text
        assert textfull.count('Кено Спортлото') == 3
        assert textfull.count('Топ 3') == 3
        assert textfull.count('ГОСЛОТО 4 из 20') == 3
        assert textfull.count('ГОСЛОТО 6 из 45') == 3
        assert textfull.count('ГОСЛОТО 7 из 49') == 3
        assert textfull.count('5х36 до тиража 7268') == 3
        assert textfull.count('Рапидо') == 6
        assert textfull.count('Рапидо2') == 3
        assert textfull.count('Спортлото 6 из 49') == 3
        assert textfull.count('Гослото 5 из 36') == 3
        assert textfull.count('Спортлото Матчбол') == 3
        assert textfull.count('6 из 36') == 3
        assert textfull.count('Русское Лото') == 3
        assert textfull.count('Жилищная лотерея') == 3
        assert textfull.count('Золотая подкова') == 3
        assert textfull.count('Бинго 80') == 3
        assert textfull.count('Бинго 75') == 3
        assert textfull.count('12x24') == 3
        assert textfull.count('Прикуп') == 3
        assert textfull.count('Дуэль') == 3
        assert textfull.count('Зодиак') == 3
        assert textfull.count('Джокер') == 3
        assert textfull.count('Моментальные') == 3
        assert 'Продажи' in textfull
        assert 'Отмены' in textfull
        assert 'Выплаты' in textfull
        assert textfull.count('ИТОГО') == 1
        assert textfull.count('Итого') == 3
        assert 'ИТОГО ПО ОТЧЕТУ' in textfull
        assert textfull.find(mskf)
        assert textfull.find(lokf)
        return textfull
        # print(re.findall('Рапидо', textfull))

# ------------------------------------------------------------------

# ------ клики по кнопкам:

    def comeback_main_page(self):
        wd = self.app.wd
        # click comeback
        wd.find_element_by_css_selector("a.btn.btn_transperent").click()
        # click close modal window
        wd.find_element_by_css_selector("a.modal__body-close").click()


    def button_get_report(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("button.btn.btn_save").click()


    def open_page_report(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("span.icon.icon-reports").click()

# -------------------------------------------------------------------------

# -------- методы для определения даты С:

    def current_day_C(self):
        d = f"{datetime.today():%d/%m/%Y 00:00:00}"
        c = f"C:  {d}"
        # print(c)
        return c


    def current_month_C(self):
        dm = f"{datetime.today():%m/%Y 00:00:00}"
        cm = f"C:  01/{dm}"
        # print(cm)
        return cm


    def previous_month_C_day_10(self):
        pmc = datetime.today()
        last_month = f"{pmc.replace(month=pmc.month - 1, day=10):%d/%m/%Y 00:00:00}"
        last_month_c = f"C:  {last_month}"
        # print(last_month)
        return last_month_c


    def previous_month_C_day_1(self):
        pmc = datetime.today()
        last_month = f"{pmc.replace(month=pmc.month - 1, day=1):%d/%m/%Y 00:00:00}"
        last_month_c = f"C:  {last_month}"
        # print(last_month)
        return last_month_c


    def beginning_of_the_week_C(self):
        tdb = datetime.today()
        m = tdb - timedelta(datetime.weekday(tdb))
        monday = f"{m:%d/%m/%Y 00:00:00}"
        return monday


    def previous_month_C_monday_from_day_10(self):
        pmc = datetime.today()
        last_month = pmc.replace(month=pmc.month - 1, day=10)
        m = last_month - timedelta(datetime.weekday(last_month))
        mondayc = f"{m:%d/%m/%Y 00:00:00}"
        return mondayc


# ------------------------------------------------------------------------

# -------- методы для определения даты ПО:

    def current_day_Po(self):
        dp = f"{datetime.today():%d/%m/%Y %H:%M}"
        Po = f"По: {dp}"
        # print(Po)
        return Po


    def previous_month_Po_day_10(self):
        pmp = datetime.today()
        last_month = f"{pmp.replace(month=pmp.month - 1, day=10):%d/%m/%Y 23:59:59}"
        last_month_po = f"По: {last_month}"
        # print(last_month_po)
        return last_month_po


    def previous_month_Po_lastday(self):
        date_now = datetime.today()
        previous_month = date_now.replace(month=date_now.month - 1)
        last_day = previous_month.replace(day=calendar.monthrange(previous_month.year, previous_month.month)[1])
        last_day_month = f"{last_day:%d/%m/%Y 23:59:59}"
        # print(last_day_month)
        return last_day_month


    def previous_month_Po_sunday_from_monday(self):
        pmp = datetime.today()
        last_month = pmp.replace(month=pmp.month - 1, day=10)
        sp = last_month - timedelta(datetime.weekday(last_month))
        s = sp.replace(day=sp.day + 6)
        sunday = f"{s:%d/%m/%Y 23:59:59}"
        return sunday


# -------------------------------------------------------------------------------

# ------------- селекты, чекбоксы:

    def without_checkbox_cash_report(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='reportType1']").click()


    def select_checkbox_for_month(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='reportType3']").click()


    def select_checkbox_since_the_beginning_of_the_week(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='reportType4']").click()


    def select_checkbox_for_the_week(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='reportType5']").click()


    def select_user(self):
        wd = self.app.wd
        wd.find_element_by_name("reportUserType").click()
        wd.find_element_by_css_selector("option[value='USER']").click()

# -----------------------------------------------------------------------------

# --------- клики за предыдущий месяц:

    def previous_month_date_10(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(
            "a.react-datepicker__navigation.react-datepicker__navigation--previous").click()
        wd.find_element_by_xpath("(//div[@aria-label='day-10'])").click()


    def previous_month_date_1(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(
            "a.react-datepicker__navigation.react-datepicker__navigation--previous").click()
        wd.find_element_by_xpath("(//div[@aria-label='day-1'])").click()

# ---------------------------------------------------------------------------------------