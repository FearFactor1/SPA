# Тест: Ввод логина через экранную клавиатуру



def test_screen_keyboard(app2):
    app2.login.press_keyboard() # ввод логина через экранную клавиатуру
    app2.login.enter_button()
    app2.login.user_in_main_page()
    app2.session.exit_spa()