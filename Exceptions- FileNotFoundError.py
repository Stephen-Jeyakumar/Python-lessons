# Exceptions
# 11-27-2020
# FileNotFoundError

filename = 'banana.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    message = print("That file called " + filename + ' cannot be found. Try again.')