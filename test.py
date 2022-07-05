import keyring
import json
import requests
import os

token = os.environ.get('DUSTICO_API_TOKEN')

test = os.environ.get('TEST_SECRET')

url = "https://api.dusti.co/v1/packages"

headers = {
    "Authorization": f"token {token}"
}
data = [
    {
        "name": "node-ipc",
        "type": "npm",
        "version": "9.2.2",
    }
]
r = requests.post(url, json=data, headers=headers)
r.raise_for_status()
print(json.dumps(r.json(), indent=2))

print(test)
#testings stuff