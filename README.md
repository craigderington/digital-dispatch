# digital-dispatch
Digital Dispatch OWL Demo Script

This console app will attempt to automate the submission of test data for the Digital Dispatch OWL demo trial.

The app reads a CSV data file, gets the first row, builds a dictionary from the CSV data, json encodes the data and sets up requests to send a POST and PUT request to the following endpoints:

* [POST] https://portal.owlsite.net/api/tankdata
* [PUT] https://portal.owlsite.net/api/tanks/1279

The POST request submits data to frontend_tankdatahistory

The PUT request updates the individual tank with the most recent receiver time, sensor value and network ID.


