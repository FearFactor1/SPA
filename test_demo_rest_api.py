from requests import post
from requests.auth import HTTPBasicAuth
from datetime import datetime
import re
import base64
import json
from wheezy.core.luhn import luhn_checksum
import hashlib
import ssl
import socket


login = ""
password = ""
auth = (login, password)

url = ""
data = 'TERMINAL_ID=2000006810&REQUEST_TIME=1&LOGIN=20003511&PASSWORD=75374377'

url_33 = ""
DATE_START = f"{datetime.today():%Y.%m.%d+03}"
data_33 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=4&GAME_ID=7103&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'


url_33_2 = ""
data_33_2 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=2&GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'
data_33_3 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=7&GAME_ID=7103&DATE_START="{DATE_START}"&DRAW_ID=2200&DRAWS_NUMBER=5&VERSION=1'


URL_40 = ""
DATA_40_BONUS_PRICE = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&VERSION=1&BONUS_FLAG=1&N_GAME_ID=2&GAME_ID[0]=4420&GAME_ID[1]=5536'


URL_UTIL_49 = ""
DATA_GETLIST_UTIL_49 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&COMMAND="Utilization/GetList"&DATA="eyJ1c2VyTnVtYmVyIjoiMjAwMDM1MTEiLCJ0ZXJtaW5hbE51bWJlciI6IjIwMDAwMDY4MTAiLCJzaWduIjoiNzgxYTdkZGE2NWMyZDdhMTQzYjRjYzFkZDUwMGUwNTFlY2MzMDYzZCIsImdhbWVUeXBlIjoiNzEwMyIsImRyYXciOiIxMzI2In0="'


def test_assertpos():
    response = post(url=url, data=data, auth=HTTPBasicAuth(*auth))
    response = response.text
    print(response)
    #status_code = response.status_code
    #assert status_code == 200


def test_message_id_33_results_and_prize():
    response = post(url=url_33, data=data_33, auth=HTTPBasicAuth(*auth))
    response = response.text.split('\n')
    for row in response:
        if 'draw_id' in row:
            draw = row.replace('<draw_id>', '').replace('</draw_id>', '').strip()
            draw_r = f"ЛОТО 4/20 - Тираж {draw} :"
            print(draw_r)
    for row in response:
        if 'win_numbers' in row:
            win = row.replace('<win_numbers>', '').replace('</win_numbers>', '').strip()
            print(win)
    return draw_r
    return win


def test_message_id_33_last_4_draws():
    draw_id = '<draw_id>(.*?)</draw_id>'
    win_numbers = '<win_numbers>(.*?)</win_numbers>'
    response = post(url=url_33_2, data=data_33_2, auth=HTTPBasicAuth(*auth))
    response = response.text
    d = re.findall(draw_id, response)
    w = re.findall(win_numbers, response)
    assert f"ЛОТО 4/20 - Тираж {d[0]} :"
    assert f"ЛОТО 4/20 - Тираж {d[1]} :"
    assert f"ЛОТО 4/20 - Тираж {d[2]} :"
    assert f"ЛОТО 4/20 - Тираж {d[3]} :"
    # Проверка: Если в  w(win_numbers) прилетает '""' ,
    # то удаляю строку так-как на экране больше не отображается '""'
    for s in w[:]:
        if '""' in w:
            w.remove(s)
    ws = w
    for ss in ws[:]:
        assert ss in ws
    print(d)
    print(ws)


def test_message_id_33_russianlott_winning_numbers_for_5_draws():
    range_90 = [i for i in range(1, 91)]
    draw_id = '<draw_id>(.*?)</draw_id>'
    win_numbers = '<win_numbers>(.*?)</win_numbers>'
    response = post(url=url_33_2, data=data_33_3, auth=HTTPBasicAuth(*auth))
    response = response.text
    d = re.findall(draw_id, response)
    wn = re.findall(win_numbers, response)
    missing_numbers_1 = []
    missing_numbers_2 = []
    missing_numbers_3 = []
    missing_numbers_4 = []
    missing_numbers_5 = []
    split_numbers_list_1 = wn[0].split()
    split_numbers_list_2 = wn[1].split()
    split_numbers_list_3 = wn[2].split()
    split_numbers_list_4 = wn[3].split()
    split_numbers_list_5 = wn[4].split()
    assert f"РУССКОЕ ЛОТО - Тираж {d[0]} :"
    assert f"РУССКОЕ ЛОТО - Тираж {d[1]} :"
    assert f"РУССКОЕ ЛОТО - Тираж {d[2]} :"
    assert f"РУССКОЕ ЛОТО - Тираж {d[3]} :"
    assert f"РУССКОЕ ЛОТО - Тираж {d[4]} :"
    # Проверка: Если в  w(win_numbers) прилетает '""' ,
    # то удаляю строку так-как на экране больше не отображается '""'
    for s in wn[:]:
        if '""' in wn:
            wn.remove(s)
    ws = wn
    for ss in ws[:]:
        assert ss in ws
    # Невыпавшие числа алгоритм
    if '""' not in wn:
        for i in range_90:
            if str(i) not in split_numbers_list_1:
                missing_numbers_1.append(i)
            if str(i) not in split_numbers_list_2:
                    missing_numbers_2.append(i)
            if str(i) not in split_numbers_list_3:
                    missing_numbers_3.append(i)
            if str(i) not in split_numbers_list_4:
                    missing_numbers_4.append(i)
            if str(i) not in split_numbers_list_5:
                    missing_numbers_5.append(i)
        print(d)
        print(ws)
        print(missing_numbers_1)
        print(missing_numbers_2)
        print(missing_numbers_3)
        print(missing_numbers_4)
        print(missing_numbers_5)


def test_message_id_40_bonus_price_in_main_page():
    b = []
    bonus_price = '<bonus_price>(.*?)</bonus_price>'
    response = post(url=URL_40, data=DATA_40_BONUS_PRICE, auth=HTTPBasicAuth(*auth))
    response = response.text
    bp = re.findall(bonus_price, response)
    for i in bp:
        s = i[:-2]
        b.append(s)
    print(b)


def test_control_number():
    """Функция формирования контрольного числа для билета"""

    list_tickets = 7175044000010061
    control_number = luhn_checksum(list_tickets)
    print(control_number)


def test_json_base64_encode():
    info = '{"userNumber":"",' \
           '"terminalNumber":"",' \
           '"sign":"",' \
           '"gameType":"7103",' \
           '"draw":"1326"}'
    enc = info.encode()
    bas = base64.encodebytes(enc)
    print(bas)


def test_sha1():
    # логига формирования sign от поба
    s = sorted(['20003511', '2000006810', '7115', '0258'])
    sl = ''.join(s)
    hash_object = hashlib.sha1(sl.encode())
    hex_dig = hash_object.hexdigest()
    print(hex_dig)


def test_getlist_utilization():
    game_type = "7105"
    draw = "0412"
    s = sorted(['20003511', '2000006810', f'{game_type}', f'{draw}'])
    sl = ''.join(s)
    hash_object = hashlib.sha1(sl.encode())
    hex_dig = hash_object.hexdigest()
    info_d = str([{'"userNumber"': '""',
                 '"terminalNumber"': '""',
                 '"sign"': f'"{hex_dig}"',
                 '"gameType"': f'"{game_type}"',
                 '"draw"': f'"{draw}"'}])
    info_re = re.sub(r"[']", "", info_d).replace('[', '').replace(']', '')
    enc = info_re.encode()
    bas = base64.encodebytes(enc)
    strbas = str(bas).replace("b'", "")
    unescape = bytes(strbas, "utf-8").decode("unicode_escape")
    DATA_GETLIST_UTIL = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&COMMAND="Utilization/GetList"&DATA={unescape}'
    response = post(url=URL_UTIL_49, data=DATA_GETLIST_UTIL, auth=HTTPBasicAuth(*auth))
    response = response.text.split('\n')
    di = str(response)[36:].replace("']", "")
    decode = base64.b64decode(di)
    diccode = json.loads(decode)
    for k, v in diccode.items():
        print(k, v)


def test_ssl():

    import requests
    from urllib3.util.ssl_ import create_urllib3_context
    from requests.adapters import HTTPAdapter

    cert_path = "C:\\PycharmProjects\\seleniumpython\\ssl\\tranc.crt"
    private_key_path = "C:\\PycharmProjects\\seleniumpython\\ssl\\terminal_id.key"
    passphrase_key = "1234"

    class SSLAdapter(HTTPAdapter):

        def init_poolmanager(self, *args, **kwargs):
            context = create_urllib3_context()
            context.load_cert_chain(certfile=cert_path, keyfile=private_key_path, password=passphrase_key)
            kwargs['ssl_context'] = context
            return super().init_poolmanager(*args, **kwargs)

    session = requests.Session()
    session.verify = False  # If you don't want to validate server's public certificate
    session.mount("", SSLAdapter())
    response = session.post("",
                            json={'terminalId': 0, 'nGameId': 1, 'gameId': [5101]})
    print(response.json())