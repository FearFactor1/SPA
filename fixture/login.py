from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from requests import post
from requests.auth import HTTPBasicAuth
from fixture.messages import MessageID
import re
from selenium.common.exceptions import NoSuchElementException
import time

# ----------- Глобальные переменные:

login = ""
password = ""
auth = (login, password)
bonus_price = '<bonus_price>(.*?)</bonus_price>'
BONUS_PHONE_BALANCE_VALUE = 'BALANCE_VALUE=(.*?)&REQUEST_SIGN=0'
TOTAL_AMOUNT = '<totalAmount>(.*?)</totalAmount>'
REQUEST_SIGN_50 = 'REQUEST_SIGN=(.*?)&GAME_ID'
PRODUCT_ID = '<product_id>(.*?)</product_id>'
BONUS_PRICE = '<bonus_price>(.*?)</bonus_price>'
TERMINAL_ID = "2000006810"
LOGIN = "20003511"
PASSWORD = "75374377"


# --------------------------------------


class LoginHelper:

    def __init__(self, app):
        self.app = app

    # -------- основные методы login

    def invisible_button(self):
        wd = self.app.wd
        # клик на поле логин и пароль, проверка, что поле Войти не доступна
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("password").click()
        submit = wd.find_element_by_css_selector("button.btn.btn_submit.selenium_btn_submit")
        disabled_search = submit.get_attribute("disabled")
        assert disabled_search is not None
        wd.find_element_by_xpath("(//button[@disabled=''])")
        WebDriverWait(wd, 5).until_not(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn_submit.selenium_btn_submit"))
        )
        wd.get_screenshot_as_file('C:\\PycharmProjects\\SPA\\screen\\login\\login_invisible_button.png')

    def correct_user(self):
        # обычный ввод логина и пароля
        wd = self.app.wd
        self.app.open_home_page()
        hellow = wd.find_element_by_css_selector("h1.signIn__header-head").text
        assert hellow == "Представьтесь, кто вы?"
        faq = wd.find_element_by_css_selector("div.signIn__footer").text
        assert "© 2011–2020 «Столото». По вопросам работы системы звоните" in faq
        assert "+7 (900) 614-55-55" in faq
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("20003511")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("75374377")
        wd.get_screenshot_as_file('C:\\PycharmProjects\\SPA\\screen\\login\\correct_user.png')

    def user_in_main_page(self):
        # парсер, вытаскивает текст из тегов, информация и пользователе на главной страницы спа
        wd = self.app.wd
        WebDriverWait(wd, 5).until(
            EC.text_to_be_present_in_element(
                (
                    By.CSS_SELECTOR, "div.header__user-data-text-number.header__user-data-text-number_small"),
                "20003511")
        )
        for text_info_user in wd.find_elements_by_css_selector(
                "li.header__user-data-item.header__user-data-item_user"):
            info_text = text_info_user.text.split('\n')
        return info_text

    def support_info_in_main_page(self):
        # парсер, вытаскивает текст из тегов, информация о тех.поддержке на главной страницы спа
        wd = self.app.wd
        for text_info_support in wd.find_elements_by_css_selector(
                "li.header__user-data-item.header__user-data-item_phone"):
            support_text = text_info_support.text.split('\n')
        return support_text

    def data_in_main_page(self):
        # Проверка даты и время на главной страницы спа
        wd = self.app.wd
        datem = f"{datetime.today():%d.%m.%Y}"
        mskm = f"{datetime.today():%H:%M:%S MSK}"
        lokfm = f"{datetime.today():%H:%M:%S ЛОК}"
        if len(wd.find_element_by_css_selector("div.header__date").text) > 0:
            textdate = wd.find_element_by_css_selector("div.header__date").text
        assert datem in textdate
        assert mskm in textdate
        assert lokfm in textdate

    def err_passwword(self):
        wd = self.app.wd
        WebDriverWait(wd, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.signIn__error"))
        )
        # wd.find_element_by_css_selector("div.signIn__error").click()
        return wd.find_element_by_css_selector("div.signIn__error").text
        # wd.find_element_by_xpath(".//*[text()='0051 Неверный идентификатор пользователя терминала']/..")

    def balance_text_in_main_page(self):
        wd = self.app.wd
        for text_info_balance in wd.find_elements_by_css_selector(
                "li.header__user-data-item.header__user-data-item_balance > div > div.header__user-data-text-number"):
            info_text_balance = text_info_balance.text
        print(info_text_balance)
        return info_text_balance.replace(" ", "")

    def exit_cancel_exit(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("span.icon.icon-exit").click()
        exit_text = wd.find_element_by_css_selector("h1.modal__head").text
        assert "Вы уверены, что вы\nхотите выйти?" in exit_text
        wd.find_element_by_css_selector("a.btn.btn_transperent.btn_arround").click()

    def parser_bonus_price_in_main_page(self, gameid):
        wd = self.app.wd
        text_bonus = []
        for text_info_bonus_price in wd.find_elements_by_css_selector("li.games__list-unit"):
            text_bonus.append(text_info_bonus_price.text)
        auth = (login, password)
        response = post(url="http://ga-s3-lcp.ga.stoloto.su/fprov/fcgi_pos?message_id=40",
                        data=f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&VERSION=1&BONUS_FLAG=1&'
                             f'N_GAME_ID=2&GAME_ID[0]={gameid}&GAME_ID[1]={gameid}',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        # код игры прилетает
        pi = " ".join(re.findall(PRODUCT_ID, response))
        # цена в бонусах игры
        bpf = " ".join(re.findall(BONUS_PRICE, response))
        # если у игры несколько тиражей активны, то может прилететь цена в бонусах каждого тиража,
        # нужен только первый(текущий),
        sfn = bpf.split(" ", 1)
        bp = sfn[0]
        # Проверка если бонус прайс из гейта прилетит 0, то ошибка
        #        for bprice in bp:
        #            if bprice == '0'
        # В зависимости от кода игры, делаем проверку:
        if pi == "4420":
            assert f'«Спортлото «4 из 20»\n{bp[:-2]}' in text_bonus[0]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "5536":
            assert f'«Спортлото «5 из 36»\n{bp[:-2]}' in text_bonus[1]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "5101":
            assert f'«Спортлото «6 из 45»\n{bp[:-2]}' in text_bonus[2]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "5150":
            assert f'«Спортлото «7 из 49»\n{bp[:-2]}' in text_bonus[3]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "5550":
            assert f'«Спортлото Матчбол»\n{bp[:-2]}' in text_bonus[4]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "28005":
            assert f'«Зодиак»\n{bp[:-2]}' in text_bonus[5]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "7103":
            assert f'«Русское лото»\n{bp[:-2]}' in text_bonus[6]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "7105":
            assert f'«Жилищная лотерея»\n{bp[:-2]}' in text_bonus[7]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "7115":
            assert f'«Золотая подкова»\n{bp[:-2]}' in text_bonus[8]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "7175":
            assert f'«Бинго-75»\n{bp[:-2]}' in text_bonus[9]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "7101":
            assert f'«6 из 36»\n{bp[:-2]}' in text_bonus[10]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "5211":
            assert f'«Рапидо»\n{bp[:-2]}' in text_bonus[11]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "5212":
            assert f'«Рапидо 2.0»\n{bp[:-2]}' in text_bonus[12]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "28001":
            assert f'«12/24»\n{bp[:-2]}' in text_bonus[13]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "28003":
            assert f'«Дуэль»\n{bp[:-2]}' in text_bonus[14]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "28102":
            assert f'«Джокер»\n{bp[:-2]}' in text_bonus[15]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "2177":
            assert f'«Топ-3»\n{bp[:-2]}' in text_bonus[16]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus
        elif pi == "1124":
            assert f'«КЕНО-Спортлото»\n{bp[:-2]}' in text_bonus[17]
            assert "«Типографские билеты»" in text_bonus
            assert "«Моментальные»" in text_bonus

    def test_check_href_in_docunents_menu(self):
        wd = self.app.wd
        assert wd.find_element_by_css_selector("h3.docs__head").text == "Программное обеспечение и документация"
        for text_href_documents in wd.find_elements_by_css_selector("ul.docs__list"):
            text_documents = text_href_documents.text
        return text_documents

    def assert_href_arms3_small_doc(self):
        wd = self.app.wd
        # current_url = wd.current_url
        current_url = ""
        wd.find_element_by_link_text("АРМ S3 Краткая инструкция пользователя").click()
        assert "http://download.russian-lotteries.net/public1/ARMS3ShortManual.pdf" == wd.current_url
        wd.get(current_url)

    def assert_href_arms3_full_doc(self):
        wd = self.app.wd
        # current_url = wd.current_url
        current_url = ""
        wd.find_element_by_link_text("АРМ S3 Полная инструкция пользователя").click()
        assert "http://download.russian-lotteries.net/public1/ARMS3FullMmanual.pdf" == wd.current_url
        wd.get(current_url)

    def assert_href_arms3_pipo_doc(self):
        wd = self.app.wd
        # current_url = wd.current_url
        current_url = ""
        wd.find_element_by_link_text("АРМ S3 Инструкция пользователя для PIPO").click()
        assert \
            "http://download.russian-lotteries.net/public1/ARM_S3_PIPO_instrukciya_polzovatelya.pdf" == wd.current_url
        wd.get(current_url)

    def assert_href_rostelecom_doc(self):
        wd = self.app.wd
        # current_url = wd.current_url
        current_url = ""
        wd.find_element_by_link_text("Инструкция (Ростелеком)").click()
        assert "http://download.russian-lotteries.net/public1/Rostelekom_instrukcija.pdf" == wd.current_url
        wd.get(current_url)

    def assert_href_tele2_doc(self):
        wd = self.app.wd
        # current_url = wd.current_url
        current_url = ""
        wd.find_element_by_link_text("Инструкция (Теле2)").click()
        assert "http://download.russian-lotteries.net/public1/Tele2_instrukcija.pdf" == wd.current_url
        wd.get(current_url)

    def assert_href_update_sert_doc(self):
        wd = self.app.wd
        # current_url = wd.current_url
        current_url = ""
        wd.find_element_by_link_text("Инструкция по обновлению сертификата").click()
        assert "http://download.russian-lotteries.net/public1/Client_Cert_Manual.pdf" == wd.current_url
        wd.get(current_url)

    # ----------------------------------------------------------------------------------------------------------

    # ------------- клики по кнопкам:

    def enter_button(self):
        # нажатие на кнопку войти
        wd = self.app.wd
        wd.find_element_by_css_selector("button.btn.btn_submit").click()

    def incorrect_user(self):
        wd = self.app.wd
        self.app.open_home_page()
        # Ввод не правильного юзера
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("2000351")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("34756381")
        wd.get_screenshot_as_file('C:\\PycharmProjects\\SPA\\screen\\login\\incorrect_user.png')

    def press_keyboard(self):
        wd = self.app.wd
        # press login and password on keyboard
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("")
        wd.find_element_by_xpath("//body").click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("")
        wd.find_element_by_xpath("//body").click()
        # метод который принимает логин и пароль, делает клики по экранной клавеатуре
        wd.find_element_by_css_selector(".selenium_keyboard_username").click()
        lg_in_menu_for_key = wd.find_elements_by_css_selector(".keyboard-nums__num")
        for lg in LOGIN:
            for keyb in lg_in_menu_for_key:
                if lg == keyb.text:
                    keyb.click()
        wd.find_element_by_css_selector("button.btn.btn_transperent").click()
        # Прокликивание пароля через экранную клавиатуру
        wd.find_element_by_css_selector(".selenium_keyboard_password").click()
        ps_in_menu_for_key = wd.find_elements_by_css_selector(".keyboard-nums__num")
        for ps in PASSWORD:
            for keyb in ps_in_menu_for_key:
                if ps == keyb.text:
                    keyb.click()
        wd.find_element_by_css_selector("button.btn.btn_transperent").click()
        wd.get_screenshot_as_file('C:\\PycharmProjects\\SPA\\screen\\login\\login_keyboard.png')

    def click_balance_in_main_page(self):
        wd = self.app.wd
        time.sleep(3)
        WebDriverWait(wd, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "li.header__user-data-item.header__user-data-item_balance > "
                                  "div.header__user-data-text > div.header__user-data-text-number"))
        ).click()
        time.sleep(3)

    #        wd.find_element_by_css_selector(
    #            "li.header__user-data-item.header__user-data-item_balance > div.header__user-data-text > "
    #            "div.header__user-data-text-number").click()

    def click_bonus_price_in_main_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("button.header-black-link__unit").click()
        time.sleep(3)

    def click_show_more_in_main_page(self):
        wd = self.app.wd
        try:
            wd.find_element_by_css_selector("div.js-nav-list-show-more").click()
        except NoSuchElementException:
            pass

    def click_bonus_check_in_main_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("span.icon.icon-bonus").click()

    def click_win_check_in_main_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("span.icon.icon-docs").click()

    def press_phone_bonus(self, PLAYER_INFO):
        wd = self.app.wd
        # метод который принимает телефон и сделает клики по экранной клавеатуре
        phone_in_menu_for_key = wd.find_elements_by_css_selector(".js__keyboard-num")
        for ph in PLAYER_INFO:
            for keyb in phone_in_menu_for_key:
                if ph == keyb.text:
                    keyb.click()
        wd.find_element_by_css_selector("button.btn.btn_transperent").click()

    def bonus_balance_in_modal_window(self):
        wd = self.app.wd
        modal_head = wd.find_element_by_css_selector("div.modal__body.modal__body_small > h1.modal__head").text
        print(modal_head)
        return modal_head

    def close_bonus_modal_phone(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a.modal__body-close").click()

    def click_ok_bonus_modal_window(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.modal__body.modal__body_small > button.btn.btn_transperent").click()

    def click_settings_in_main_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("span.icon.icon-settings").click()

    def click_all_settings(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("label[for='checkbox']").click()
        wd.find_element_by_css_selector("label[for='fiscal']").click()
        wd.find_element_by_css_selector("label[for='winprint']").click()
        wd.find_element_by_css_selector("label[for='isCurrency']").click()
        wd.find_element_by_css_selector("label[for='keepSlip100loto']").click()
        wd.find_element_by_css_selector("button.btn.btn_save.settings-confirm").click()

    def press_unique_key_positive(self, ticketid):
        wd = self.app.wd
        wd.find_element_by_name("barcode").send_keys(ticketid)
        wd.find_element_by_css_selector("button.btn.btn_transperent").click()
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.payout__check-result"))
        )
        win = wd.find_element_by_css_selector("div.payout__check-result").text.replace(' ', '')
        print(win)
        return win

    def press_unique_key_negative(self, ticketid):
        wd = self.app.wd
        wd.find_element_by_name("barcode").send_keys(ticketid)
        wd.find_element_by_css_selector("button.btn.btn_transperent").click()
        WebDriverWait(wd, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.error-message"))
        )
        win = wd.find_element_by_css_selector("div.error-message").text
        print(win)
        return win
        wd.find_element_by_css_selector("a.modal__body-close").click()

    def click_documents_in_main_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Документация").click()

    def click_back_main_page_in_documents_menu(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("a.docs__back").click()

    # ------------------------------------------------------

    # ------------- Отправка запросов в gate:

    def send_message_id_5(self):
        auth = (login, password)
        response = post(url=MessageID.URL_5, data=MessageID.DATA_BALANCE, auth=HTTPBasicAuth(*auth))
        response = response.text
        tbv = response[29:-2] + "₽"
        print(tbv)
        return tbv

    def send_message_id_64(self, PLAYER_INFO):
        auth = (login, password)
        response = post(url=MessageID.URL_64,
                        data=f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&PLAYER_INFO=7{PLAYER_INFO}',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        bpbv = " ".join(re.findall(BONUS_PHONE_BALANCE_VALUE, response))
        if bpbv == '0':
            tbpbv = f'Бонусный баланс: 0'
            print(tbpbv)
            return tbpbv
        tbpbv = f'Бонусный баланс: {bpbv[:-2]}'
        print(tbpbv)
        return tbpbv

    def send_message_id_50_sum_win_positive(self, ticketid):
        auth = (login, password)
        response = post(url="",
                        data=f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&ID_TICKET_TYPE=1&' \
                             f'BARCODE="00000 00000 00000 00000 00000 00000 00000"&TICKET_ID={ticketid}&'
                             f'TAX_DEDUCTION_REQUESTED=0',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        ta = " ".join(re.findall(TOTAL_AMOUNT, response))
        if ta == '0':
            tavf = f'Выигрыш{ta}рублей\nВыплатить'
            print(tavf)
            return tavf
        else:
            tav = sum(list(map(int, ta.split())))
            tavf = f'Выигрыш{str(tav)[:-2]}рублей\nВыплатить'
            print(tavf)
            return tavf

    def send_message_id_50_sum_win_negative(self, ticketid):
        auth = (login, password)
        response = post(url="",
                        data=f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&ID_TICKET_TYPE=1&' \
                             f'BARCODE="00000 00000 00000 00000 00000 00000 00000"&TICKET_ID={ticketid}&'
                             f'TAX_DEDUCTION_REQUESTED=0',
                        auth=HTTPBasicAuth(*auth))
        response = response.text
        ta = " ".join(re.findall(REQUEST_SIGN_50, response))
        if ta == '4465':
            tavf = f'{ta} Без выигрыша'
            print(tavf)
            return tavf
        elif ta == '4417':
            tavf = f'{ta} Билет отменен'
            print(tavf)
            return tavf
        elif ta == '83':
            tavf = f'00{ta} Уже выплачено'
            print(tavf)
            return tavf
        elif ta == '4464':
            tavf = f'{ta} Срок выплаты выигрыша истёк'
            print(tavf)
            return tavf

# ------------------------------------------------------
