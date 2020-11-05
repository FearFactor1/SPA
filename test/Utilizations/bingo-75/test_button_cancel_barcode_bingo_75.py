# Пишем баркод в первое поле ввода, нажимаем кнопку Отмена, смотрим, что меню утилизации пустое


def test_button_cancel_barcode_bingo_75(app, fixture_barcode_bingo75):
    app.utiliz.open_page_utilization()
    app.utiliz.click_bingo_75()
    app.utiliz.modal_draw_ok()
    app.utiliz.button_add()
    app.utiliz.modal_one_input_ticket_barcode(fixture_barcode_bingo75)
    app.utiliz.modal_ticket_barcode_cancel()
    assert app.utiliz.barcode_not_in_util_menu() == 0
    app.utiliz.comeback_main_page()