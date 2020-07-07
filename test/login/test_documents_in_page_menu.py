# тест для проверки всех ссылок и текста в меню документация с3



def test_check_documents(app2):
    app2.login.correct_user()
    app2.login.enter_button()
    app2.login.click_show_more_in_main_page()
    # Переход в Документацию с3
    app2.login.click_documents_in_main_page()
    # Текст из документации: названия инструкций, ссылок, обём в МБ
    app2.login.test_check_href_in_docunents_menu()
    assert "АРМ S3 Краткая инструкция пользователя(pdf, 3,11 МБ)" in app2.login.test_check_href_in_docunents_menu()
    # Переход в инструкцию арм с3 краткая и проверка url инструкции, возврат обратно из pdf
    app2.login.assert_href_arms3_small_doc()
    # возвращаемся в документацию для проверки остальных инструкций
    app2.login.click_show_more_in_main_page()
    app2.login.click_documents_in_main_page()
    assert "АРМ S3 Полная инструкция пользователя(pdf, 6,77 Мб)" in app2.login.test_check_href_in_docunents_menu()
    app2.login.assert_href_arms3_full_doc()
    app2.login.click_show_more_in_main_page()
    app2.login.click_documents_in_main_page()
    assert "АРМ S3 Инструкция пользователя для PIPO(pdf, 4,7 Мб)" in app2.login.test_check_href_in_docunents_menu()
    app2.login.assert_href_arms3_pipo_doc()
    app2.login.click_show_more_in_main_page()
    app2.login.click_documents_in_main_page()
    assert "Драйвер сканера (Windows)( v2.4.0.0, zip, 14,2 Мб)" in app2.login.test_check_href_in_docunents_menu()
    assert "Драйвер сканера (Linux)( v2.4.0.0, x-sh, 2,31 Мб)" in app2.login.test_check_href_in_docunents_menu()
    assert "Инструкция (Ростелеком)(pdf, 1,9 Мб)" in app2.login.test_check_href_in_docunents_menu()
    app2.login.assert_href_rostelecom_doc()
    app2.login.click_show_more_in_main_page()
    app2.login.click_documents_in_main_page()
    assert "Инструкция (Теле2)(pdf, 2,0 Мб)" in app2.login.test_check_href_in_docunents_menu()
    app2.login.assert_href_tele2_doc()
    app2.login.click_show_more_in_main_page()
    app2.login.click_documents_in_main_page()
    assert "UmkaLite РМК(v1.3.0, exe, 19,5 Мб)" in app2.login.test_check_href_in_docunents_menu()
    app2.login.click_back_main_page_in_documents_menu()
    app2.session.exit_spa()