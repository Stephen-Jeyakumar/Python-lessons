# Miscellaneous
# 11-29-2020
# Testing Code 2

# Building off of Testing Code 1

from Miscellaneous_Testing_Code import get_formatted_name
print("Enter 'q' to quit the program")

while True:
    first = input("\nFirst Name:")
    if first == 'q':
        break
    last = input("\nLast Name:")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("Hallo there organism named " + formatted_name + "! \nRemember to press 'q' to quit the program!")


    