from datetime import datetime



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
        wd.find_element_by_xpath("(//input[@disabled='disabled'])")
        wd.get_screenshot_as_file('C:\\PycharmProjects\\SPA\\screen\\login\\login_invisible_button.png')
        wd.find_element_by_xpath("(//input[@type='submit'])").is_displayed()


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
        wd.find_element_by_css_selector("span.icon.icon-keyboard.modal-link-local").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(2)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(11)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(11)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(11)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(3)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(5)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(1)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(11)").click()
        wd.find_element_by_class_name("btn.btn_transperent.modal__prompt").click()
        # Прокликивание пароля через экранную клавиатуру
        wd.find_element_by_css_selector("span.icon.icon-keyboard.modal-link-local.modal-link-local_password").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(3)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(4)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(7)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(5)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(6)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(3)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(8)").click()
        wd.find_element_by_css_selector("div.keyboard-nums__row > div:nth-child(1)").click()
        wd.find_element_by_class_name("btn.btn_transperent.modal__prompt").click()
        wd.get_screenshot_as_file('C:\\PycharmProjects\\S3\screen\\login\\login_keyboard.png')


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
        wd.get_screenshot_as_file('C:\\PycharmProjects\\S3\screen\\login\\incorrect_user.png')


    def correct_user(self):
        # обычный ввод логина и пароля
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("20003510")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("34756381")
        wd.get_screenshot_as_file('C:\\PycharmProjects\\S3\screen\\login\\correct_user.png')


    def user_in_main_page(self):
        # проверка, что на главной странице s3, отображается пользователь и терминал
        wd = self.app.wd
        user = wd.find_element_by_css_selector("div.header__user-data-text-head_user").text
        assert "Пользователь:" in user
        wd.find_element_by_xpath("//*/div[contains(text(), '20003510')]")
        wd.find_element_by_xpath("//*/div[contains(text(), '2000006809')]")
        dat_s3 = wd.find_element_by_css_selector("div.header__date-day").text
        dat_tmz = datetime.today().strftime('%Y.%m.%d')
        assert dat_s3 == dat_tmz


    def enter_button(self):
        # нажатие на кнопку войти
        wd = self.app.wd
        wd.find_element_by_css_selector("div > input[value='Войти']").click()


    def err_passwword(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("div.signIn__error.signIn__error_show.error").text
        #wd.find_element_by_xpath(".//*[text()='0051 Неверный идентификатор пользователя терминала']/..")