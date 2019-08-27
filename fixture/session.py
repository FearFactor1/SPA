


class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath(u"//input[@value='Войти']").click()
        wd.get_screenshot_as_file('C:\\PycharmProjects\\S3\\screen\\session\\login.png')


    def exit_s3(self):
        wd = self.app.wd
        # click to exit s3
        wd.find_element_by_class_name("icon.icon-exit").click()
        wd.find_element_by_class_name("cashboxLogout.btn.btn_transperent").click()
        wd.get_screenshot_as_file('C:\\PycharmProjects\\S3\\screen\\session\\exit_s3.png')


    def ensure_exit_s3(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.exit_s3()


    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_class_name("icon.icon-exit")) > 0


    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_css_selector("div.header__user-data-text-head_user").text == "("+username+")"


    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.exit_s3()
        self.login(username, password)


    def assertion_current_page(self):
        wd = self.app.wd
        return wd.current_url







