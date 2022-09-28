# !/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------
# _Description_ = Simple Python script to call the dustico scs api.  
# _Version_ =  1.0.0
# _Author_ = Sean Casey
# _Credits_ = [Jossef Harush, Tzachi Zorenshtain, Checkmarx SCS Team]
# _Status_ = Development
# -----------------------------------------------------------------

import keyring
import json
import requests
import os


# ***** Description *****
# Simple Python script to call the dustico scs api.  Currently only using package.json as the manifest file.
# The script takes the dependencies json from the package.json and converts it into an acceptable format for the body of the api request.
# User can define the path of the package.json and the results file.
# Future updates: hoping to include other manifest files and also include html and pdf options!
# **********************
# _Version_ =  1.0.0
# _Author_ = Sean Casey
# _Status_ = Development




# SECRETS 
# - When local I am using Windows Credentials with keyring
# - Secrets are also stored in Github for Github Actions
# - Using os.environ with Windows Environment variables is not secure
# - Comment out the secrets declarations depending on what you are doing

# Keyring Secrets
token = keyring.get_password(u":local-database:scs", u"token")
url = keyring.get_password(u":local-database:scs-url", u"url")
manifestPath = 'package.json'

# NAme of the Results File.  Default is scs_results.json
resultsFileName = 'scs_results.json'

# Github Actions
# token = os.environ.get('DUSTICO_API_TOKEN')
# url = os.environ.get('DUSTICO_API_URL')
# manifestPath = os.environ.get('MANIFEST_PATH')
# resultsFileName = os.environ.get('RESULTS_FILE_NAME')

# Empty list to store the converted json for the API request.
scs_data = []

headers = {
    "Authorization": "token " + token
}

try:
    # Opening JSON file
    f = open(manifestPath)
    # returns JSON object as a dictionary
    data = json.load(f)  

except:
    print('Cannot find the package.json.  Please check the manifestPath')
  

try:
    dependencies = data['dependencies']
except:
    print('No dependencies were found. Check the manifest file.')


for key in dependencies:
    
    scs_data.append({"name": key,"type": "npm","version": dependencies[key]})
    
    pass

try:
    r = requests.post(url, json=scs_data, headers=headers)
    r.raise_for_status()
    print(json.dumps(r.json(), indent=2))
except:
    print('Something went wrong')

try:
    # Write Results out to a Json File
    with open(resultsFileName,'w') as outfile:
        json.dump(r.json(),outfile)
except:
    print('There was an issue writing out to the results file')
    print('please make sure the results file is in a folder that has write permissions and the resultsFileName is a .json file')








