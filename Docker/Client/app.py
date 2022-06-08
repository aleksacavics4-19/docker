import json
import http.client

connection = http.client.HTTPConnection("localhost:5000")
objectPayload = json.dumps(
  {'ime': 'Aleksa',
  'prezime': 'Cavic',
  'username': 'acavic',
  'smer': 'IT',
  'predmeti':
    [{'ime': 'AIOS', 'espb': 8},
     {'ime': 'Osnovi programiranja', 'espb': 8},
     {'ime': 'WSIT', 'espb': 8}
    ]}
)
headers = {
  'Content-Type': 'application/json'
}

connection.request("POST", "/users", objectPayload, headers)
response = connection.getresponse()
dataDisplay = response.read()
print(dataDisplay.decode("utf-8"))