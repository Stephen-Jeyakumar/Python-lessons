# Files
# 11-24-2020
# Working with a File's Content

# Same code as Making a list from a File, but adding new stuf and modifying it.

filename = 'Random_Examples.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

popped_movies = lines.pop()

for line in lines:
    print(line.strip())


print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

sorted_movies = lines.sort()

for line in lines:
    print(line.strip())
