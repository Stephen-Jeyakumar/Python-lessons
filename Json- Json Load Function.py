# Json
# 11-28-2020
# Json Load Function

import json

filename = 'phone_number.json'

with open(filename) as file_object:
    phone_number = json.load(file_object)

print(phone_number)