# Json
# 11-28-2020
# Json Dump Function

import json

phone_number = [1234567890]

filename = 'phone_number.json'

with open(filename, 'w') as file_object:
    json.dump(phone_number, file_object)