#! .env/bin/python

import config
import requests
from requests.auth import HTTPBasicAuth
import json

payload = {
    "network_id": "ORLFL01_7077",
    "service_address": 1276,
    "receiver_time": "2017-01-04 13:16:17",
    "sensor_value": "38.39"
}

try:
    s = requests.Session()
    s.auth = ('digitaldispatch', 'owlsitedemo')
    s.headers.update({'x-test': 'true', 'X-CSRFToken': '7BY4ZQHQTXRuL4FrmuVQGb1GqtBi6EIR'})
    r = s.get('http://localhost:5880/api-auth/login/',
              auth=HTTPBasicAuth(username=config.loginusername, password=config.loginpassword),
              headers=s.headers)
    csrftoken = r.cookies['csrftoken']

    # Interact with the API.
    tank_id = 1243
    response = requests.put('http://localhost:5880/api/tanks/' + str(tank_id) + '/',
                            auth=HTTPBasicAuth(username=config.loginusername, password=config.loginpassword),
                            headers={'X-CSRFToken': csrftoken},
                            data=payload)

    if response.status_code == 200:
        print(response.content)
    else:
        print(response.content)

except requests.HTTPError as e:
    print 'HTTPError'



