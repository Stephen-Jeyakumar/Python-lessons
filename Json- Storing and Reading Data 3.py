# Json
# 11-29-2020
# Storing and Reading Data 3(All combined)

import json

filename = 'username.json'

try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input('What is your username?')
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        print("I will remember you alwaysssss " + username + '.') 
else:
    print("Welcome " + username + '.\nI told you I will remember you foreverrrrr...')