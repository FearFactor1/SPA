from requests import post
from requests.auth import HTTPBasicAuth


login = "s3_http_access"
password = "ambush!Tidy4"

url = "http://ga-s3-lcp.ga.stoloto.su/fprov/fcgi_pos?message_id=5"
data = 'TERMINAL_ID=2000006810&REQUEST_TIME=1&LOGIN=20003511&PASSWORD=75374377'
auth = (login, password)


def test_assertpos():
    response = post(url=url, data=data, auth=HTTPBasicAuth(*auth))
    response = response.text
    print(response)
    #status_code = response.status_code
    #assert status_code == 200
