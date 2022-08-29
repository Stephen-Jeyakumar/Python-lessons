# Files
# 11-24-2020
# Making a List from a File 

""" It is thanksgiving break time!!!!! My school break starts today!!! I am happy!!!"""

filename = 'Random_Examples.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
