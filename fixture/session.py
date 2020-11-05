


class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_css_selector("button.btn.btn_submit").click()
        wd.get_screenshot_as_file('C:\\PycharmProjects\\S3\\screen\\session\\login.png')

    def exit_spa(self):
        wd = self.app.wd
        # click to exit spa
        wd.find_element_by_css_selector("span.icon.icon-exit").click()
        wd.find_element_by_css_selector("button.btn.btn_transperent.btn_arround").click()
        wd.get_screenshot_as_file('C:\\PycharmProjects\\S3\\screen\\session\\exit_s3.png')

    def ensure_exit_spa(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.exit_spa()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("span.icon.icon-exit")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_css_selector("div.header__user-data-text-head_user").text == "("+username+")"

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.exit_spa()
        self.login(username, password)

    def assertion_current_page(self):
        wd = self.app.wd
        return wd.current_url