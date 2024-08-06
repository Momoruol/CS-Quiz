import requests
import json

api = 'https://opentdb.com/api.php'

parameters = {
    'amount': 10,
    "type": 'boolean',
    'category': 18
}

connection = requests.get(api, params=parameters)
data = connection.json()

question_data = data['results']
