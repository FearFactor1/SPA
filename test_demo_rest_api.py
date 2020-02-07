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
data_33 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=5&GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'


url_33_2 = "http://ga-s3-lcp.ga.stoloto.su/fprov/fcgi_pos?message_id=33"
data_33_2 = f'TERMINAL_ID=2000006810&LOGIN=20003511&PASSWORD=75374377&REPORT_TYPE=2&GAME_ID=4420&DATE_START="{DATE_START}"&DRAW_ID=0&DRAWS_NUMBER=0&VERSION=1'




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



