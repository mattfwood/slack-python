import requests
import json

url = 'http://127.0.0.1:5000/'
payload = {'message': 'python message'}

r = requests.post('http://127.0.0.1:5000/', data=json.dumps(payload))

# show response
# print r.text
# print r.status_code
