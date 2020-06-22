# Тест: Проверка отображения бонусов на главном экране СПА после нажатия на кнопку Цены в бонусах
from selenium.webdriver.common.keys import Keys
import pytest



@pytest.mark.parametrize('gameid', ['4420', '5536', '5101', '5150', '5550', '28005', '7103', '7105', '7115', '7175',
                                    '7101', '5211', '5212', '28001', '28003', '28102', '2177', '1124'])
def test_show_bonus_price_main_page(app2, gameid):
    app2.login.correct_user()
    app2.login.enter_button()
    app2.login.click_bonus_price_in_main_page()
    app2.login.parser_bonus_price_in_main_page(gameid)
    app2.session.exit_spa()