import json

car_dictionary = {
    'name': 'tesla',
    'engine': '90000kj',
    'type': 'electric'
}

# print(type(car_dictionary))

# json.dumps(dict_obj) --> string
    # use this to create JSON string fromour dictionairies
car_data_json_string = json.dumps(car_dictionary)
# print(type(car_data_json_string))

# json.dump(dict_object, file) --> writes json to a file
with open('new_json_file.json', 'w') as jsonfile:
    json.dump(car_dictionary, jsonfile)

# json.load(jsonfile) --> dictionary
with open('new_json_file.json', 'r') as jsonfile:
    car = json.load(jsonfile)
    print(car['name'])

