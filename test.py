import keyring
import json
import requests
import os

token = os.environ.get('DUSTICO_API_TOKEN')

test = os.environ.get('TEST_SECRET')

print(test)