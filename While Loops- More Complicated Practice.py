# While Loops
# 11-2-2020
# More complicated practice

rental_properties = {}
# Flag, to acknowledge we are taking applications 
rental_open = True

while rental_open:
    # Asks users for name and address
    username = input("\n What is your name?")
    rental_property = input("What is the address of the property that you have to rent?")

    # storing the responses inside a dictionary
    rental_properties[username] = rental_property

    # asks user if they know anyone else trying to rent a property
    repeat = input("\n Do you know anyone else who would like to rent out their property? (say no otherwise you will have to repeat this whole thing again)")
    if repeat == 'no':
        rental_open = False
    # adding property is complete

print("\n ******Property To Rent******")
for username, rental_property in rental_properties.items():
    print(username + ' has ' + rental_property + " to rent.")