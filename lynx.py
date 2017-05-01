#! .env/bin/python

import os
import sys
import csv
import json
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import lynx_config as config


def main():
    """
    Lynx Propane Software OWL Demo Trial
    Send a POST and PUT request to the OWL API for tank_id 1279 - Digital Dispatch
    :param: none
    :type: main() console app
    :return: json
    """

    # the tank ID
    tank_id = config.tank_id

    # first, open the data file and read the first line
    with open(config.file_path, 'r') as f:
        try:
            reader = csv.reader(f)
            next(f)
            row = next(reader)
            payload = {
                'tank': row[1],
                'network_id': row[2],
                'mtu_id': row[2].split('_')[1:],
                'receiver_time': str(datetime.now()),
                'sensor_value': row[4],
                'service_address': 1346
            }

            hdr = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-CSRFToken": config.Token
            }

            url_1 = 'https://portal.owlsite.net/api/tankdata/'
            url_2 = 'https://portal.owlsite.net/api/tanks/' + str(tank_id) + '/'

            auth = HTTPBasicAuth(config.loginusername, config.loginpassword)

            try:
                # post the data to tank data history
                r1 = requests.post(url_1, headers=hdr, auth=auth, json=payload)

                if r1.status_code == 201:
                    print('SUCCESS! ' + r1.content)

                    # update the tank with the latest sensor value
                    r2 = requests.put(url_2, headers=hdr, auth=auth, json=payload)

                    if r2.status_code == 200:
                        print('SUCCESS! ' + r2.content)

                        # open the file and write out the remaining rows
                        try:
                            with open(config.file_path, 'w') as f1:
                                writer = csv.writer(f1)
                                writer.writerows(reader)
                        except csv.Error as e:
                            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

                    else:
                        print('FAIL R2: HTTP returned a ' + str(r2.status_code) + ' status code.')

                else:
                    print('FAIL R1: HTTP returned a ' + str(r1.status_code) + ' status code.')

            except requests.HTTPError as e:
                print('Sorry, a communication error has occurred ' + str(e))

        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


if __name__ == '__main__':
    main()
