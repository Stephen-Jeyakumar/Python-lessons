# Files
# 11-25-2020
# Appending to a File

message = input("What is your favorite animal?")
print(message)

filename = 'Favorite_Animal.txt'

with open(filename, 'a') as file_object:
    file_object.write(message + '\n')