#! .env/bin/python

import config
import requests
from requests.auth import HTTPBasicAuth
import json

payload = {
    "network_id": "ORLFL01_7077",
    "service_address": 1312,
    "receiver_time": "2017-01-04 13:16:17",
    "sensor_value": "38.39"
}

try:
    s = requests.Session()
    s.auth = (config.loginusername, config.loginpassword)
    s.headers.update({'x-test': 'true', 'X-CSRFToken': config.Token})
    r = s.get('http://localhost:5880/api-auth/login/',
              auth=HTTPBasicAuth(username=config.loginusername, password=config.loginpassword),
              headers=s.headers)

    # Interact with the API.
    tank_id = config.tank_id
    response = requests.put('http://localhost:5880/api/tanks/' + str(tank_id) + '/',
                            auth=HTTPBasicAuth(username=config.loginusername, password=config.loginpassword),
                            headers={'X-CSRFToken': config.Token},
                            data=payload)

    if response.status_code == 200:
        print(response.content)
    else:
        print(response.content)

except requests.HTTPError as e:
    print 'HTTPError'



