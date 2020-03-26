from requests import post
from requests.auth import HTTPBasicAuth
from datetime import datetime
import re




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
    assert w[0] in response
    assert w[1] in response
    assert w[2] in response
    assert w[3] in response
    print(d)
    print(w)


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
    assert wn[0] in response
    assert wn[1] in response
    assert wn[2] in response
    assert wn[3] in response
    assert wn[4] in response
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
        print(wn)
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
    tlb = '7103012980100000449'
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
