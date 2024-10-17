import requests
import json

access_token = 'YTdjMTE2N2ItMmE4MC00YzhjLTlkZDYtOWYwNjk4ZDUyMWE0OTY4YTFhYTQtNjNj_P0A1_1ad92174-dfe2-4740-b008-57218895946c'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
