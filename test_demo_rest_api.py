from requests import post
from requests.auth import HTTPBasicAuth
from datetime import datetime
import re
import base64
import json




login = "s3_http_access"
password = "ambush!Tidy4"
auth = (login, password)

url = "http://ga-s3-lcp.ga.stoloto.su/fprov/fcgi_pos?message_id=5"
data = 'TERMINAL_ID=2000006810&REQUEST_TIME=1&LOGIN=20003511&PASSWORD=75374377'

url_33 = "http://ga-s3-lcp.ga.stoloto.su/fprov/fcgi_pos?message_id=33"
DATE_START = f"{datetime.today():%Y.%m.%d+03}"
data_33 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=4&GAME_ID=7103&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'


url_33_2 = "http://ga-s3-lcp.ga.stoloto.su/fprov/fcgi_pos?message_id=33"
data_33_2 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=2&GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'
data_33_3 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=7&GAME_ID=7103&DATE_START="{DATE_START}"&DRAW_ID=2200&DRAWS_NUMBER=5&VERSION=1'


URL_40 = "http://ga-s3-lcp.ga.stoloto.su/fprov/fcgi_pos?message_id=40"
DATA_40_BONUS_PRICE = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&VERSION=1&BONUS_FLAG=1&N_GAME_ID=2&GAME_ID[0]=4420&GAME_ID[1]=5536'





URL_UTIL_49 = "http://ga-s3-lcp.ga.stoloto.su/fprov/fcgi_pos?message_id=49"
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




def test_algoritm_luna():
    tlb = [7101024000010069]
    mult_numb = [2, 1]
    i = 0
    sum_of_digits = 0
    for s in tlb:
        for d in str(int(s) * mult_numb[i]):
            sum_of_digits += int(d)
        i = (i + 1) % 2
    a = (10 - sum_of_digits % 10) % 10
    tlb_luna = str(tlb) + str(a)
    print(tlb_luna)





def test_json_base64_encode():
    info = '{"userNumber":"20003511","terminalNumber":"2000006810","sign":"781a7dda65c2d7a143b4cc1dd500e051ecc3063d","gameType":"7103","draw":"1326"}'
    enc = info.encode()
    bas = base64.encodebytes(enc)
    print(bas)






sign_6x36 = "df7ee0c229e55b9eca9586ce2012c518f10ced7a"
sign_zp = "aca913a4d46c156026793ba05bd31b76803f9506"
sign_rl = "d6b52860878393d8c02c80ec6da4545fec316419"
sign_zl = "a4989730df61308a09cdcd07049a76f22f377871"

def test_getlist_Utilization():
    info = '{"userNumber":"20003511","terminalNumber":"2000006810","sign":"8757af7ccbfd0babf49a0b8a2cf6bda2876883ec","gameType":"7175","draw":"0370"}'
    enc = info.encode()
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






