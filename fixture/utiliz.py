import time


class UtilizHelper:

    def __init__(self, app):
        self.app = app

    # ------- клики по кнопкам:

    def open_page_utilization(self):
        # Открыть меню утилизации на главном экране с3
        wd = self.app.wd
        wd.find_element_by_css_selector(".nav-list__item_utilization").click()

    def comeback_main_page(self):
        # возврат на главное меню с3
        wd = self.app.wd
        time.sleep(2)
        wd.find_element_by_css_selector("a.modal__body-close").click()

    def button_add(self):
        # кнопка Добавить в меню утилизации
        wd = self.app.wd
        time.sleep(2)
        wd.find_element_by_css_selector(".btn.btn_link.btn_transperent").click()

    def modal_draw_ok(self):
        # кнопка Ок в модальном окне при выборе тиража игры
        wd = self.app.wd
        assert wd.find_element_by_css_selector("h1.modal__head").text == "Введите значение"
        wd.find_element_by_link_text("Ок").click()

    def modal_draw_ok_icon(self):
        #  кнопка Ок в модальном окне калькулятора при вводе баркода
        wd = self.app.wd
        assert wd.find_element_by_css_selector(".modal__body_small h1.modal__head").text == "Введите значение"
        wd.find_element_by_css_selector(".modal__body_small button.btn.btn_transperent").click()

    def modal_ticket_barcode_add(self):
        # Кнопка добавить в модольном окне ввода баркода
        wd = self.app.wd
        wd.find_elements_by_css_selector("div.btn.btn_transperent")[1].click()

    def modal_ticket_barcode_cancel(self):
        # Кнопка отменить в модальном окне ввода баркода
        wd = self.app.wd
        wd.find_elements_by_css_selector("div.btn.btn_transperent")[0].click()

    def click_keyboard_icon(self):
        # клик по калькулятору в первом поле ввода баркода
        wd = self.app.wd
        wd.find_element_by_css_selector(":nth-child(3) > button.keyboard-icon").click()

    def click_keyboard_icon_2(self):
        # клик по калькулятору во втором поле ввода баркода
        wd = self.app.wd
        wd.find_element_by_css_selector(":nth-child(4) > button.keyboard-icon").click()

    def click_two_input_in_keyboard(self):
        # клик по второму полю на экранной клавиатуре
        wd = self.app.wd
        wd.find_element_by_name("drawTo").click()

    # ------------------------------------------------------------------------------------------

    # ------ выбрать игру в меню утилизации:

    def click_bingo_75(self):
        wd = self.app.wd
        assert wd.find_element_by_css_selector("h2").text == "Выберите игру"
        wd.find_element_by_css_selector(".utilization-game_7175").click()

    # --------------------------------------------------------------------------------------------

    # -------- модальные окна:

    def modal_one_input_ticket_barcode(self, fixture_barcode_bingo75):
        # Модальное окно ввода первого баркода
        wd = self.app.wd
        assert wd.find_element_by_css_selector(".modal__head").text == "Штрихкод билета:"
        wd.find_element_by_name("drawFrom").send_keys(fixture_barcode_bingo75)

    def modal_two_input_ticket_barcode(self, fixture_barcode_bingo75_2):
        # модальное окно ввода второго баркода
        wd = self.app.wd
        assert wd.find_element_by_css_selector(".modal__head").text == "Штрихкод билета:"
        wd.find_element_by_name("drawTo").send_keys(fixture_barcode_bingo75_2)

    def modal_one_input_ticket_barcode_keyboard(self, fixture_barcode_bingo75):
        # метод который принимает баркод и сделает клики по экранной клавеатуре
        wd = self.app.wd
        bar_in_menu_for_key = wd.find_elements_by_css_selector(".js__keyboard-num")
        for br in fixture_barcode_bingo75:
            for keyb in bar_in_menu_for_key:
                if br == keyb.text:
                    keyb.click()

    def modal_two_input_ticket_barcode_keyboard(self, fixture_barcode_bingo75_2):
        # метод который принимает баркод и сделает клики по экранной клавеатуре
        wd = self.app.wd
        bar_in_menu_for_key = wd.find_elements_by_css_selector(".js__keyboard-num")
        for br in fixture_barcode_bingo75_2:
            for keyb in bar_in_menu_for_key:
                if br == keyb.text:
                    keyb.click()

    def modal_one_input_ticket_barcode_keyboard_icon(self, fixture_barcode_bingo75):
        # метод который принимает баркод и сделает клики по экранной клавеатуре калькулятора
        wd = self.app.wd
        bar_in_menu_icon_for_key = wd.find_elements_by_css_selector(".modal__body_small button.keyboard-nums__num")
        for bri in fixture_barcode_bingo75:
            for keyb in bar_in_menu_icon_for_key:
                if bri == keyb.text:
                    keyb.click()

    def modal_two_input_ticket_barcode_keyboard_icon(self, fixture_barcode_bingo75_2):
        # метод который принимает баркод и сделает клики по экранной клавеатуре калькулятора
        wd = self.app.wd
        bar_in_menu_icon_for_key = wd.find_elements_by_css_selector(".modal__body_small button.keyboard-nums__num")
        for bri in fixture_barcode_bingo75_2:
            for keyb in bar_in_menu_icon_for_key:
                if bri == keyb.text:
                    keyb.click()

    # -----------------------------------------------------------------------------------------------

    # ------- методы когда купон в меню утилизации:

    def barcode_in_util_menu(self):
        # возвращает текст в виде баркода 1-2 в меню утилизации
        wd = self.app.wd
        bt = []
        time.sleep(2)
        bar_in_menu = wd.find_elements_by_css_selector("tr.cart__tr")
        for bar_text in bar_in_menu:
            bt.append(bar_text.text)
        return bt

    def barcode_not_in_util_menu(self):
        # возращаем массив тега tr.cart__tr, проверка что нет билетов в меню утилизации
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector("tr.cart__tr")) == 0

    def count_range_barcode_in_util_menu(self):
        # возвращает сколько билетов в меню утилизации в виде текста
        wd = self.app.wd
        time.sleep(2)
        bar_in_menu = wd.find_elements_by_css_selector("td")[3]
        return bar_in_menu.text

    def delete_barcode(self, fixture_barcode_bingo75):
        # динамичный кликер по экранной клавиатуре, какой баркод прилетит тот и прокликает
        wd = self.app.wd
        bar_in_menu_for_del = wd.find_elements_by_css_selector("tr.cart__tr")
        but_del = wd.find_elements_by_css_selector(".btn_delete")
        for br_del in bar_in_menu_for_del:
            if f'{fixture_barcode_bingo75} {fixture_barcode_bingo75} 1' == br_del.text:
                but_del[-1].click()

    def two_delete_barcode(self, fixture_barcode_bingo75, fixture_barcode_bingo75_2):
        # если баркод в менб утилизации, то удаляется последний баркод
        wd = self.app.wd
        bar_in_menu_for_del = wd.find_elements_by_css_selector("tr.cart__tr")
        but_del = wd.find_elements_by_css_selector(".btn_delete")
        for br_del in bar_in_menu_for_del:
            if f'{fixture_barcode_bingo75} {fixture_barcode_bingo75_2} {self.count_range_barcode_in_util_menu()}' \
                    == br_del.text:
                but_del[-1].click()

    def show_draw_in_util_menu(self):
        # возвращает тираж из меню утилизации
        wd = self.app.wd
        assert wd.find_element_by_css_selector("span.utilization__game-item.utilization__game-item_7175")
        text_menu = wd.find_element_by_css_selector("h1.cart__head").text
        return text_menu

    def get_input_value(self):
        # берём тираж из модального окна выбора тиража
        wd = self.app.wd
        draw_in_input = wd.find_element_by_css_selector(".input-num").get_attribute("value")
        return f'Утилизация для тираж {draw_in_input}'

    # -----------------------------------------------------------------------------------------------
