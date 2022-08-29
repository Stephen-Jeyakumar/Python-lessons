# Json
# 11-29-2020
# Storing and 'Reading' Data 2

# And it will output here

import json

filename = 'username.json'

with open(filename) as file_object:
    username = json.load(file_object)
    print("Welcome " + username + '.\nI told you I will remember you foreverrrrr...')