import keyring
import json
import requests
import os
import pdfkit
import markdown
import fileinput

# token = keyring.get_password(u":local-database:scs", u"token")
token = os.environ.get('DUSTICO_API_TOKEN')

options = {
  "enable-local-file-access": None
}


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

md = markdown.Markdown()

# Write Results out to a Json File
with open('scs_results.json','w') as outfile:
    json.dump(r.json(),outfile)
#testings stuff

packageContent = ''
for a in r.json():
    # print(a['name'])
    packageContent = packageContent + '<div class="package-container"><div class="package-header"><div class="package-icon"><img src="images/npm-logo.png" /></div><div class="package-title"><h1>' + a['name'] + '</h1><h3>' + a['version'] + '</h3></div></div></div>'

    if len(a['risks']):
        for x in a['risks']:
            test44 = md.convert(x['description'])
            print(test44)


with fileinput.FileInput('template.html', inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace('<p>test</p>', packageContent), end='')


print(pdfkit.from_file('template.html', 'out.pdf',options=options))