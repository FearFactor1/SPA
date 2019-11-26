from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginHelper:

    def __init__(self, app):
        self.app = app

# ----- основные методы фикстуры login

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
        date_spa_main_page = wd.find_element_by_css_selector("div.header__date-day").text
        date_spa = datetime.today().strftime('%d.%m.%Y')
        assert date_spa_main_page == date_spa
        time_msk_main_page = wd.find_element_by_css_selector("div.header__date-timeMsk").text
        time_msk = datetime.today().strftime('%H:%M:%S') + " MSK"
        assert time_msk in time_msk_main_page
        time_lok_main_page = wd.find_element_by_css_selector("div.header__date-timeLoc").text
        time_lok = datetime.today().strftime('%H:%M:%S') + " ЛОК"
        assert time_lok in time_lok_main_page


    def enter_button(self):
        # нажатие на кнопку войти
        wd = self.app.wd
        wd.find_element_by_css_selector("button.btn.btn_submit").click()


    def err_passwword(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.signIn__error").click()
        return wd.find_element_by_css_selector("div.signIn__error").text
        # wd.find_element_by_xpath(".//*[text()='0051 Неверный идентификатор пользователя терминала']/..")