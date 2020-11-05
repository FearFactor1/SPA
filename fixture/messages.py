from datetime import datetime, timedelta


class MessageID:

    def __init__(self, app):
        self.app = app

    # переменная DATE_START - текущая дата для запросов
    DATE_START = f"{datetime.today():%Y.%m.%d+03}"
    # переменная DATE_START_CURRENT_MONTH_ML - текущий месяц для запросов 32
    DATE_START_CURRENT_MONTH_ML = f"{datetime.today():%Y.%m.01+03}"
    # Адрес запроса 33  - результаты и призы
    URL_33 = ""
    URL_32 = ""
    TERMINAL_ID = ""
    LOGIN = ""
    PASSWORD = ""
    PLAYER_INFO = ""


# ---------------- message_id=5:

    # message_id=5, запрос баланса терминала в гейт
    URL_5 = ""
    DATA_BALANCE = f'TERMINAL_ID={TERMINAL_ID}&REQUEST_TIME=1&LOGIN={LOGIN}&PASSWORD={PASSWORD}'

# -----------------------------------------------------------------------------------------

# ---------------- message_id=40:

    URL_40 = ""
    DATA_40_BONUS_PRICE = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&VERSION=1&BONUS_FLAG=1&' \
                          f'N_GAME_ID=18&GAME_ID[0]=4420&GAME_ID[1]=5536&GAME_ID[2]=5101&GAME_ID[3]=5150&' \
                          f'GAME_ID[4]=5550&GAME_ID[5]=28005&GAME_ID[6]=7103&GAME_ID[7]=7105&GAME_ID[8]=7115&' \
                          f'GAME_ID[9]=7175&GAME_ID[10]=7101&GAME_ID[11]=5211&GAME_ID[12]=5212&GAME_ID[13]=28001&' \
                          f'GAME_ID[14]=28003&GAME_ID[15]=28102&GAME_ID[16]=2177&GAME_ID[17]=1124'


# --------------------------------------------------

# ---------------- message_id=64:

    # message_id=64, запрос состояния бонусного счета участника
    URL_64 = ""
#    DATA_64_BONUS_BALANCE = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&PLAYER_INFO={PLAYER_INFO}'

# -----------------------------------------------------------------------------------------

# ---------------- message_id=50:

    # message_id=50, Информационный запрос размера выигрыша по лотерейному билету с учетом налога, message_id=50
#    URL_50 = "http://ga-s3-lcp.ga.stoloto.su/fprov/fcgi_pos?message_id=50"
#    DATA_50_TOTAL_AMOUNT = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&ID_TICKET_TYPE=1&' \
#                           f'BARCODE="00000 00000 00000 00000 00000 00000 00000"&TICKET_ID={TICKET_ID}&TAX_DEDUCTION_REQUESTED=0'

# -----------------------------------------------------------------------------------------

# message_id=32 для отчётов:
# ---------------- message_id=32:
    # Отчёт за текущий месяц
    DATA_32_REPORT_TYPE_1031 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1031&' \
                               f'REPORT_USER={LOGIN}&REPORT_TERMINAL={TERMINAL_ID}&' \
                               f'DATE_START="{DATE_START_CURRENT_MONTH_ML}"'

    # Отчёт за текущий день
    DATA_32_REPORT_TYPE_1030 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1030&' \
                               f'REPORT_USER={LOGIN}&REPORT_TERMINAL={TERMINAL_ID}&' \
                               f'DATE_START="{DATE_START}"'

    # Отчёт за текущий день по пользователю
    DATA_32_REPORT_TYPE_518 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=518&' \
                               f'REPORT_USER={LOGIN}&REPORT_TERMINAL={TERMINAL_ID}&' \
                               f'DATE_START="{DATE_START}"'

    # Отчёт за текущий месяц по пользователю
    DATA_32_REPORT_TYPE_519 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=519&' \
                               f'REPORT_USER={LOGIN}&REPORT_TERMINAL={TERMINAL_ID}&' \
                               f'DATE_START="{DATE_START_CURRENT_MONTH_ML}"'


# -----------------------------------------------------------------------------------------


# message_id=33 для результатов и призов:
# --------- 4на20:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_4420 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_4420 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_4420 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_4420 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_4420 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

# --------- 5на36:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_5536 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=5536&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_5536 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=5536&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_5536 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=5536&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_5536 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=5536&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_5536 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=5536&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

# --------- 6из45:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_5101 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=5101&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_5101 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=5101&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_5101 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=5101&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_5101 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=5101&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_5101 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=5101&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

# --------- 7из49:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_5150 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=5150&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_5150 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=5150&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_5150 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=5150&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_5150 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=5150&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_5150 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=5150&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

# --------- матчбол:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_5550 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=5550&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_5550 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=5550&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_5550 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=5550&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_5550 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=5550&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_5550 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=5550&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

# --------- Зодиак:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_28005 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                  f'GAME_ID=28005&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_28005 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                  f'GAME_ID=28005&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_28005 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                  f'GAME_ID=28005&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_28005 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                  f'GAME_ID=28005&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_28005 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                  f'GAME_ID=28005&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

# --------- Русское лото:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_7103 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=7103&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_7103 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=7103&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_7103 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=7103&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_7103 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=7103&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_7103 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=7103&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

# --------- «Русское лото Экспресс»:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_7107 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=7107&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_7107 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=7107&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_7107 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=7107&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_7107 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=7107&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_7107 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=7107&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

# --------- Жилищная лотерея:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_7105 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=7105&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_7105 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=7105&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_7105 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=7105&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_7105 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=7105&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_7105 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=7105&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

# --------- Золотая подкова:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_7115 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=7115&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_7115 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=7115&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_7115 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=7115&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_7115 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=7115&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_7115 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=7115&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

# --------- Бинго 75:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_7175 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=7175&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_7175 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=7175&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_7175 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=7175&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_7175 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=7175&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_7175 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=7175&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------


# --------- 6 из 36:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_7101 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=7101&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_7101 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=7101&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_7101 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=7101&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_7101 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=7101&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_7101 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=7101&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------


# --------- Рапидо:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_5211 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=5211&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_5211 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=5211&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_5211 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=5211&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_5211 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=5211&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_5211 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=5211&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------


# --------- Рапидо 2.0:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_5212 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=5212&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_5212 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=5212&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_5212 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=5212&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_5212 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=5212&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_5212 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=5212&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------


# --------- 12/24:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_28001 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                  f'GAME_ID=28001&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_28001 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                  f'GAME_ID=28001&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_28001 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                  f'GAME_ID=28001&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_28001 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                  f'GAME_ID=28001&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_28001 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                  f'GAME_ID=28001&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

# --------- Дуэль:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_28003 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                  f'GAME_ID=28003&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_28003 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                  f'GAME_ID=28003&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_28003 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                  f'GAME_ID=28003&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_28003 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                  f'GAME_ID=28003&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_28003 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                  f'GAME_ID=28003&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

# --------- Прикуп:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_28002 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                  f'GAME_ID=28002&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_28002 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                  f'GAME_ID=28002&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_28002 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                  f'GAME_ID=28002&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_28002 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                  f'GAME_ID=28002&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_28002 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                  f'GAME_ID=28002&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------


# --------- Джокер:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_28102 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                  f'GAME_ID=28102&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_28102 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                  f'GAME_ID=28102&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_28102 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                  f'GAME_ID=28102&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_28102 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                  f'GAME_ID=28102&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_28102 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                  f'GAME_ID=28102&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

#--------- Топ-3:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_2177 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=2177&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_2177 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=2177&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_2177 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=2177&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_2177 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=2177&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_2177 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=2177&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------

# --------- кено:

    # message_id=33, данный запрос сделан для получения последнего тиража из гейта
    DATA_33_REPORT_TYPE_1_1124 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=1&' \
                                 f'GAME_ID=1124&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения последних 4 тиражей из гейта
    DATA_33_REPORT_TYPE_2_1124 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=2&' \
                                 f'GAME_ID=1124&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата последнего тиража REPORT_TYPE_3
    DATA_33_REPORT_TYPE_3_1124 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=3&' \
                                 f'GAME_ID=1124&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения результата тиража по текущей дате REPORT_TYPE_4
    DATA_33_REPORT_TYPE_4_1124 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=4&' \
                                 f'GAME_ID=1124&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

    # message_id=33, данный запрос сделан для получения суммы суперприза
    DATA_33_REPORT_TYPE_5_1124 = f'TERMINAL_ID={TERMINAL_ID}&LOGIN={LOGIN}&PASSWORD={PASSWORD}&REPORT_TYPE=5&' \
                                 f'GAME_ID=1124&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'

# --------------------------------------------