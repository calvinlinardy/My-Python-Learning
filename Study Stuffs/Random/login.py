import requests
import json
from config import phone, password

from requests.sessions import session


def login(userName, password):
    payload = {
        'password': password,
        'userName': userName
    }
    r = requests.post('https://crm.xcyunxt.com/api/login',
                      data=json.dumps(payload))
    print(r.content)
    return r


session = login(phone, password)
