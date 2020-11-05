# Тест: Проверка отображения бонусов на главном экране СПА после нажатия на кнопку Цены в бонусах
import pytest


@pytest.mark.parametrize('gameid', ['4420', '5536', '5101', '5150', '5550', '28005', '7103', '7105', '7115', '7175',
                                    '7101', '5211', '5212', '28001', '28003', '28102', '2177', '1124'])
def test_show_bonus_price_main_page(app, gameid):
    app.login.click_bonus_price_in_main_page()
    app.login.parser_bonus_price_in_main_page(gameid)