# Files
# 11-23-2020
# Reading line by line

filename = 'Random_Examples.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.title())