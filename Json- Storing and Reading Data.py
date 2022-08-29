# Json
# 11-29-2020
# 'Storing' and Reading Data

# BTW THIS IS THE LAST DAY OF MY THANKSGIVING BREAK I AM VERY SAD SCHOOL STARTS TOMORROW :(
# Input stuff here

import json

username = input("What is your username?")

filename = 'username.json'

with open(filename, 'w') as file_object:
    json.dump(username, file_object)
    print("I will remember you alwaysss...")