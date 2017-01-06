#! .env/bin/python

import os
import sys
import csv
import json
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime


def main():
    """
    Send a PUT request to the Portal API
    :param: none
    :type: console app
    :return: json
    """

    tank_id = 1279

    # first, open the data file and read the first line
    with open('data/frontend_tankdatahistory_7077.csv', 'r') as f:
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
                'service_address': 1312
            }

            hdr = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-CSRFToken": '7BY4ZQHQTXRuL4FrmuVQGb1GqtBi6EIR'
            }

            url_1 = 'https://portal.owlsite.net/api/tankdata/'
            url_2 = 'https://portal.owlsite.net/api/tanks/' + str(tank_id) + '/'

            auth = HTTPBasicAuth('digitaldispatch', 'owlsitedemo')

            try:
                r1 = requests.post(url_1, headers=hdr, auth=auth, json=payload)
                r2 = requests.put(url_2, headers=hdr, auth=auth, json=payload)

                print(r1.content)
                print(r2.content)
                #print(payload)

                # open the file and write out the remaining rows
                try:
                    with open('data/frontend_tankdatahistory_7077.csv', 'w') as f1:
                        writer = csv.writer(f1)
                        writer.writerows(reader)
                except csv.Error as e:
                    sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

            except requests.HTTPError as e:
                print('Sorry, a communication error has occurred ' + str(e))

        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

if __name__ == '__main__':
    main()
