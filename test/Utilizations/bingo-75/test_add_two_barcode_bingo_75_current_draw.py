# Добавить диапазон билетов на утилизацию по игре бинго 75


def test_add_two_barcode_bingo_75_current_draw_range(app,
                                                     fixture_barcode_bingo75,
                                                     fixture_barcode_bingo75_2):
    app.utiliz.open_page_utilization()
    app.utiliz.click_bingo_75()
    get_value = app.utiliz.get_input_value()
    app.utiliz.modal_draw_ok()
    assert app.utiliz.show_draw_in_util_menu() == get_value
    app.utiliz.button_add()
    app.utiliz.modal_one_input_ticket_barcode(fixture_barcode_bingo75)
    app.utiliz.modal_two_input_ticket_barcode(fixture_barcode_bingo75_2)
    app.utiliz.modal_ticket_barcode_add()
    app.utiliz.barcode_in_util_menu()
    assert f'{fixture_barcode_bingo75} {fixture_barcode_bingo75_2} {app.utiliz.count_range_barcode_in_util_menu()}' \
           in app.utiliz.barcode_in_util_menu()
    app.utiliz.two_delete_barcode(fixture_barcode_bingo75, fixture_barcode_bingo75_2)
    app.utiliz.comeback_main_page()