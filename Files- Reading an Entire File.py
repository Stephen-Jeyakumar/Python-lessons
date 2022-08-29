# Files
# 11-23-2020
# Reading an entire File 

with open('Random_Examples.txt') as file_object:
    contents = file_object.read()
    print(contents.strip().title())
