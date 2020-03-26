# Тест: Проверка отображения бонусов на главном экране СПА после нажатия на кнопку Цены в бонусах




def test_show_bonus_price_main_page(app2):
    app2.login.correct_user()
    app2.login.enter_button()
    app2.login.click_bonus_price_in_main_page()
    app2.login.parser_bonus_price_in_main_page()
    assert "«Гослото «4 из 20»\n600" in app2.login.parser_bonus_price_in_main_page()
    assert "«Гослото «5 из 36»\n120" in app2.login.parser_bonus_price_in_main_page()
    assert "«Гослото «6 из 45»\n300" in app2.login.parser_bonus_price_in_main_page()
    assert "«Гослото «7 из 49»\n150" in app2.login.parser_bonus_price_in_main_page()
    assert "«Спортлото Матчбол»\n90" in app2.login.parser_bonus_price_in_main_page()
    assert "«Зодиак»\n150" in app2.login.parser_bonus_price_in_main_page()
    assert "«Русское лото»\n300" in app2.login.parser_bonus_price_in_main_page()
    assert "«Жилищная лотерея»\n300" in app2.login.parser_bonus_price_in_main_page()
    assert "«Золотая подкова»\n300" in app2.login.parser_bonus_price_in_main_page()
    assert "«Бинго-75»\n300" in app2.login.parser_bonus_price_in_main_page()
    assert "«6 из 36»\n300" in app2.login.parser_bonus_price_in_main_page()
    assert "«Рапидо»\n450" in app2.login.parser_bonus_price_in_main_page()
    assert "«Рапидо 2.0»\n180" in app2.login.parser_bonus_price_in_main_page()
    assert "«12/24»\n90" in app2.login.parser_bonus_price_in_main_page()
    assert "«Дуэль»\n90" in app2.login.parser_bonus_price_in_main_page()
    #    assert "«Джокер»\n90" in app2.login.parser_bonus_price_in_main_page()
    #    assert "«Топ-3»\n180" in app2.login.parser_bonus_price_in_main_page()
    #    assert "«КЕНО-Спортлото»\n60" in app2.login.parser_bonus_price_in_main_page()
    #    assert "«Типографские билеты»" in app2.login.parser_bonus_price_in_main_page()
    #    assert "«Моментальные»" in app2.login.parser_bonus_price_in_main_page()
    app2.session.exit_spa()