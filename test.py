import keyring
import json
import requests
import os
import wkhtmltopdf
import pdfkit


token = os.environ.get('DUSTICO_API_TOKEN')

pdfkit.from_file('template.html', 'out.pdf')



url = "https://api.dusti.co/v1/packages"

headers = {
    "Authorization": "token " + token
}

# Opening JSON file
f = open('package.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
scs_data = []

data2 = data['dependencies']

for key in data2:
    
    scs_data.append({"name": key,"type": "npm","version": data2[key]})
    
    pass

data = [
    {
        "name": "node-ipc",
        "type": "npm",
        "version": "9.2.2",
    }
]
r = requests.post(url, json=scs_data, headers=headers)
r.raise_for_status()
print(json.dumps(r.json(), indent=2))


#testings stuff