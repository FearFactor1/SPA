from datetime import datetime, timedelta



class MessageID:

    def __init__(self, app):
        self.app = app


    # message_id=5, запрос баланса терминала в гейт
    URL_5 = "http://ga-s3-lcp.ga.stoloto.su/fprov/fcgi_pos?message_id=5"
    DATA_BALANCE = 'TERMINAL_ID=2000006810&REQUEST_TIME=1&LOGIN=20003511&PASSWORD=75374377'

# -----------------------------------------------------------------------------------------

    # переменная DATE_START - текущая дата для запросов
    DATE_START = f"{datetime.today():%Y.%m.%d+03}"

    # Адрес запроса 33  - результаты и призы
    URL_33 = "http://ga-s3-lcp.ga.stoloto.su/fprov/fcgi_pos?message_id=33"

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта для игры 4на20
    DATA_33_REPORT_TYPE_1_4420 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=1&GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта для игры 4на20
    DATA_33_REPORT_TYPE_2_4420 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=2&GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_4420 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=3&GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_4420 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=4&GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_4420 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=5&GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'


