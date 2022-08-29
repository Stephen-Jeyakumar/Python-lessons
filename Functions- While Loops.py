# Functions
# 11-7-2020
# While Loops


# doesnt really work :(
    
def formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()
while True:
    print("\n What is your name?")
    first_name = input("First name: ")
    last_name = input("Last name: ")

    
    print("Hello " + formatted_name(first_name, last_name) + "!")