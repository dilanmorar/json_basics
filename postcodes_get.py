import requests

# get request
# do not have a body (json)
# they have a base url, path and arguement

base_url = 'http://api.postcodes.io/'
path = 'postcodes/'
arguement = 'mk88dt'

request_response = requests.get(base_url+path+arguement)
print(request_response)

# turning a request to dictionary --> use .json()

dictionary_response = request_response.json()
print(dictionary_response)