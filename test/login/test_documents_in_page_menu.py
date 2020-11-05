# тест для проверки всех ссылок и текста в меню документация с3


def test_check_documents(app):
    app.login.click_show_more_in_main_page()
    # Переход в Документацию с3
    app.login.click_documents_in_main_page()
    # Текст из документации: названия инструкций, ссылок, обём в МБ
    app.login.test_check_href_in_docunents_menu()
    assert "АРМ S3 Краткая инструкция пользователя(pdf, 3,11 Мб)" in app.login.test_check_href_in_docunents_menu()
    # Переход в инструкцию арм с3 краткая и проверка url инструкции, возврат обратно из pdf
    app.login.assert_href_arms3_small_doc()
    # возвращаемся в документацию для проверки остальных инструкций
    app.login.click_show_more_in_main_page()
    app.login.click_documents_in_main_page()
    assert "АРМ S3 Полная инструкция пользователя(pdf, 7,3 Мб)" in app.login.test_check_href_in_docunents_menu()
    app.login.assert_href_arms3_full_doc()
    app.login.click_show_more_in_main_page()
    app.login.click_documents_in_main_page()
    assert "АРМ S3 Инструкция пользователя для PIPO(pdf, 4,7 Мб)" in app.login.test_check_href_in_docunents_menu()
    app.login.assert_href_arms3_pipo_doc()
    app.login.click_show_more_in_main_page()
    app.login.click_documents_in_main_page()
    assert "Драйвер сканера (Windows)( v2.5.0.0, zip, 14,2 Мб)" in app.login.test_check_href_in_docunents_menu()
    assert "Драйвер сканера (Linux)( v2.5.0.0, tar, 1,8 Мб)" in app.login.test_check_href_in_docunents_menu()
    assert "Инструкция (Ростелеком)(pdf, 1,9 Мб)" in app.login.test_check_href_in_docunents_menu()
    app.login.assert_href_rostelecom_doc()
    app.login.click_show_more_in_main_page()
    app.login.click_documents_in_main_page()
    assert "Инструкция (Теле2)(pdf, 2,0 Мб)" in app.login.test_check_href_in_docunents_menu()
    app.login.assert_href_tele2_doc()
    app.login.click_show_more_in_main_page()
    app.login.click_documents_in_main_page()
    assert "UmkaLite РМК(v1.3.1, rar, 19,8 Мб)" in app.login.test_check_href_in_docunents_menu()
    assert "Инструкция по обновлению сертификата(pdf, 1,53Мб)" in app.login.test_check_href_in_docunents_menu()
    app.login.assert_href_update_sert_doc()
    app.login.click_show_more_in_main_page()
    app.login.click_documents_in_main_page()
    app.login.click_back_main_page_in_documents_menu()