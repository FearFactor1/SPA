from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from requests import post
from requests.auth import HTTPBasicAuth
from fixture.messages import MessageID
import re
from selenium.common.exceptions import NoSuchElementException


# ----------- Глобальные переменные:

login = "s3_http_access"
password = "ambush!Tidy4"
auth = (login, password)
bonus_price = '<bonus_price>(.*?)</bonus_price>'
BONUS_PHONE_BALANCE_VALUE = 'BALANCE_VALUE=(.*?)&REQUEST_SIGN=0'
TOTAL_AMOUNT = '<totalAmount>(.*?)</totalAmount>'

#--------------------------------------



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
        assert "© 2011–2019 «Столото». По вопросам работы системы звоните" in faq
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
        for text_info_user in wd.find_elements_by_css_selector(
                "li.header__user-data-item.header__user-data-item_column"):
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
        #wd.find_element_by_css_selector("div.signIn__error").click()
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


    def parser_bonus_price_in_main_page(self):
        wd = self.app.wd
        for text_info_bonus_price in wd.find_elements_by_css_selector("ul.games__list"):
            text_bonus = text_info_bonus_price.text
#        text_bonus = wd.find_element_by_css_selector("ul.games__list").text
        return text_bonus



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
        # Прокликивание логина через экранную клавиатуру
        wd.find_element_by_css_selector("button.keyboard-icon.selenium_keyboard_username").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(2)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(11)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(11)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(11)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(3)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(5)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(1)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(1)").click()
        wd.find_element_by_css_selector("button.btn.btn_transperent").click()
        # Прокликивание пароля через экранную клавиатуру
        wd.find_element_by_css_selector("button.keyboard-icon.selenium_keyboard_password").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(7)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(5)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(3)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(7)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(4)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(3)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(7)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > button:nth-child(7)").click()
        wd.find_element_by_css_selector("button.btn.btn_transperent").click()
        wd.get_screenshot_as_file('C:\\PycharmProjects\\SPA\\screen\\login\\login_keyboard.png')


    def click_balance_in_main_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(
            "li.header__user-data-item.header__user-data-item_balance > div > div.header__user-data-text-number").click()
        WebDriverWait(wd, 5).until(
            EC.invisibility_of_element((By.CSS_SELECTOR, "span.rouble"))
        )


    def click_bonus_price_in_main_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("button.header-black-link__unit").click()


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


    def press_phone_bonus(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//button[@type='button'])[9]").click()
        wd.find_element_by_xpath("(//button[@type='button'])[1]").click()
        wd.find_element_by_xpath("(//button[@type='button'])[2]").click()
        wd.find_element_by_xpath("(//button[@type='button'])[3]").click()
        wd.find_element_by_xpath("(//button[@type='button'])[4]").click()
        wd.find_element_by_xpath("(//button[@type='button'])[5]").click()
        wd.find_element_by_xpath("(//button[@type='button'])[6]").click()
        wd.find_element_by_xpath("(//button[@type='button'])[7]").click()
        wd.find_element_by_xpath("(//button[@type='button'])[8]").click()
        wd.find_element_by_xpath("(//button[@type='button'])[9]").click()
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


    def press_unique_key(self):
        wd = self.app.wd
        wd.find_element_by_name("barcode").send_keys(MessageID.TICKET_ID)
        wd.find_element_by_css_selector("button.btn.btn_transperent").click()
        WebDriverWait(wd, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.payout__check-result"))
        )
        win = (wd.find_element_by_css_selector("div.payout__check-result").text).replace(' ', '')
        print(win)
        return win



# ------------------------------------------------------

# ------------- Отправка запросов в gate:

    def send_message_id_5(self):
        auth = (login, password)
        response = post(url=MessageID.URL_5, data=MessageID.DATA_BALANCE, auth=HTTPBasicAuth(*auth))
        response = response.text
        tbv = response[29:-2]
        print(tbv)
        return tbv


    def send_message_id_64(self):
        auth = (login, password)
        response = post(url=MessageID.URL_64, data=MessageID.DATA_64_BONUS_BALANCE, auth=HTTPBasicAuth(*auth))
        response = response.text
        bpbv = " ".join(re.findall(BONUS_PHONE_BALANCE_VALUE, response))
        tbpbv = f'Бонусный баланс: {bpbv[:-2]}'
        print(tbpbv)
        return tbpbv


    def send_message_id_50_sum_win(self):
        auth = (login, password)
        response = post(url=MessageID.URL_50, data=MessageID.DATA_50_TOTAL_AMOUNT, auth=HTTPBasicAuth(*auth))
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

# ------------------------------------------------------