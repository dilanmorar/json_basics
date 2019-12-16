import requests
import json

postcode1 = input('Input postcode: ')
postcode2 = input('Input postcode: ')
postcode3 = input('Input postcode: ')

base_url = 'http://api.postcodes.io/'
path = 'postcodes/'

dictionary_postcodes = {
    'postcodes': ['mk88dt', 'ec2y5as', 'e146gt']
}

headers = {'Content-type': 'application/json'}

json_body = json.dumps(dictionary_postcodes)

postcodes_post_response = requests.post(base_url+path, data=json_body, headers=headers).json()
print(postcodes_post_response)
print(postcodes_post_response['result'][2]['result']['nhs_ha'])

print('Postcode: ' + postcode1 + ' with nhs location at: ' + postcodes_post_response['result'][0]['result']['nhs_ha'])
print('Postcode: ' + postcode2 + ' with nhs location at: ' + postcodes_post_response['result'][1]['result']['nhs_ha'])
print('Postcode: ' + postcode3 + ' with nhs location at: ' + postcodes_post_response['result'][2]['result']['nhs_ha'])

