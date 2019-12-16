import requests
import json

# post request
# need a path
# need a json object to send
# possibly headers, depending on the api

# creating the json
dictionary_postcodes = {
    'postcodes': ['ec2y5as', 'el46gt', 'ct12eh']
}

json_body = json.dumps(dictionary_postcodes)

# the url
base_url = 'http://api.postcodes.io/'
path = 'postcodes/'

# the headers
headers = {'Content-type': 'application/json'}

# making the request
postcodes_post_response = requests.post(base_url+path, data=json_body, headers = headers).json()
print(postcodes_post_response)

results = postcodes_post_response['result']['postcode']

print(results)