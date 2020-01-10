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
        # нужен для обычных лотерей
        wd = self.app.wd
        mskf = f"{datetime.today():%d/%m/%Y %H:%M:%S МСК}"
        lokf = f"{datetime.today():%d/%m/%Y %H:%M:%S МСК (ЛОК)}"
        if len(wd.find_element_by_css_selector("div.report-item").text) > 0:
            textfull = wd.find_element_by_css_selector("div.report-item").text
        assert textfull.count('Кено Спортлото') == 5
        assert textfull.count('Топ 3') == 5
        assert textfull.count('ГОСЛОТО 4 из 20') == 5
        assert textfull.count('ГОСЛОТО 6 из 45') == 5
        assert textfull.count('ГОСЛОТО 7 из 49') == 5
        assert textfull.count('5х36 до тиража 7268') == 5
        assert textfull.count('Рапидо') == 10
        assert textfull.count('Рапидо2') == 5
        assert textfull.count('Спортлото 6 из 49') == 5
        assert textfull.count('Гослото 5 из 36') == 5
        assert textfull.count('Спортлото Матчбол') == 5
        assert textfull.count('6 из 36') == 5
        assert textfull.count('Русское Лото') == 5
        assert textfull.count('Жилищная лотерея') == 5
        assert textfull.count('Золотая подкова') == 5
        assert textfull.count('Бинго 80') == 5
        assert textfull.count('Бинго 75') == 5
        assert textfull.count('12x24') == 5
        assert textfull.count('Прикуп') == 5
        assert textfull.count('Дуэль') == 5
        assert textfull.count('Зодиак') == 5
        assert textfull.count('Джокер') == 5
        assert textfull.count('Моментальные') == 5
        assert textfull.count('Продажи') == 2
        assert textfull.count('Продажи за бонусы') == 1
        assert textfull.count('Отмены') == 2
        assert textfull.count('Отмены за бонусы') == 1
        assert 'Выплаты' in textfull
        assert textfull.count('Итого :') == 5
        assert 'ИТОГО ПО ОТЧЕТУ' in textfull
        assert textfull.find(mskf)
        assert textfull.find(lokf)
        return textfull
        # print(re.findall('Рапидо', textfull))


    def parser_full_report_text_for_instant_game(self):
        # нужен для моменталок
        wd = self.app.wd
        mskml = f"{datetime.today():%d/%m/%Y %H:%M:%S МСК}"
        lokml = f"{datetime.today():%d/%m/%Y %H:%M:%S МСК (ЛОК)}"
        if len(wd.find_element_by_css_selector("div.report-item").text) > 0:
            textfullml = wd.find_element_by_css_selector("div.report-item").text
        assert textfullml.count('ИГРА' and 'НАЗВАНИЕ' and 'ПРОДАЖИ' and 'ВЫПЛАТЫ') == 1
        assert textfullml.count('30501' and 'Точно в цель') == 1
        assert textfullml.count('30502' and 'Победа+Самовол') == 1
        assert textfullml.count('30503' and 'Сапер') == 1
        assert textfullml.count('30505' and '50 на 50') == 1
        assert textfullml.find('30508' and 'Спорт без гран')
        assert textfullml.find('30509' and 'Узоры на льду')
        assert textfullml.count('30510' and 'Вперед к побед') == 1
        assert textfullml.count('30511' and 'Вершины успеха') == 1
        assert textfullml.count('30512' and 'Поехали!') == 1
        assert textfullml.count('30513' and 'Быстрее, выше,') == 1
        assert textfullml.count('30514' and 'Веселые старты') == 1
        assert textfullml.count('30515' and 'Спортивный сез') == 1
        assert textfullml.count('30516' and 'Праздник спорт') == 1
        assert textfullml.count('30517' and 'Русские игры') == 1
        assert textfullml.find('30519' and 'Спорт без гран')
        assert textfullml.find('30520' and 'Узоры на льду')
        assert textfullml.count('ИТОГО') == 1
        assert textfullml.find(mskml)
        assert textfullml.find(lokml)
        return textfullml

    def parser_full_report_text_for_typographical(self):
        # нужен для типографских
        wd = self.app.wd
        msktlb = f"{datetime.today():%d/%m/%Y %H:%M:%S МСК}"
        loktlb = f"{datetime.today():%d/%m/%Y %H:%M:%S МСК (ЛОК)}"
        if len(wd.find_element_by_css_selector("div.report-item").text) > 0:
            textfulltlb = wd.find_element_by_css_selector("div.report-item").text
        assert textfulltlb.count('Продажи') == 1
        assert textfulltlb.count('Билеты' and 'Сумма руб.') == 4
        assert textfulltlb.count('Итого :') == 4
        assert textfulltlb.count('Отмены продаж:') == 1
        assert textfulltlb.count('Выплаты') == 1
        assert textfulltlb.count('Отмены выплат') == 1
        assert textfulltlb.count('ИТОГО ПО ОТЧЁТУ:') == 1
        assert textfulltlb.find(msktlb)
        assert textfulltlb.find(loktlb)
        return textfulltlb


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
        if pmc.month == 1:
            last_month = f"{pmc.replace(month=12, day=10, year=pmc.year - 1):%d/%m/%Y 00:00:00}"
        else:
            last_month = f"{pmc.replace(month=pmc.month - 1, day=10):%d/%m/%Y 00:00:00}"
        last_month_c = f"C:  {last_month}"
        # print(last_month)
        return last_month_c


    def previous_month_C_day_1(self):
        pmc = datetime.today()
        if pmc.month == 1:
            last_month = f"{pmc.replace(month=12, day=1, year=pmc.year - 1):%d/%m/%Y 00:00:00}"
        else:
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
        if pmc.month == 1:
            last_month = pmc.replace(month=12, day=10, year=pmc.year - 1)
        else:
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
        if pmp.month == 1:
            last_month = f"{pmp.replace(month=12, day=10, year=pmp.year - 1):%d/%m/%Y 23:59:59}"
        else:
            last_month = f"{pmp.replace(month=pmp.month - 1, day=10):%d/%m/%Y 23:59:59}"
        last_month_po = f"По: {last_month}"
        # print(last_month_po)
        return last_month_po


    def previous_month_Po_lastday(self):
        date_now = datetime.today()
        if date_now.month == 1:
            previous_month = date_now.replace(month=12, year=date_now.year - 1)
        else:
            previous_month = date_now.replace(month=date_now.month - 1)
        last_day = previous_month.replace(day=calendar.monthrange(previous_month.year, previous_month.month)[1])
        last_day_month = f"{last_day:%d/%m/%Y 23:59:59}"
        # print(last_day_month)
        return last_day_month


    def previous_month_Po_sunday_from_monday(self):
        pmp = datetime.today()
        if pmp.month == 1:
            last_month = pmp.replace(month=12, day=10, year=pmp.year - 1)
        else:
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


    def select_instant_lottery(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("select.select.report__select").click()
        wd.find_element_by_css_selector("option[value='instant']").click()


    def select_typographical(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("select.select.report__select").click()
        wd.find_element_by_css_selector("option[value='printed']").click()


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