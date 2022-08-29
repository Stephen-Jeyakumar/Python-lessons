# Functions
# 11-8-2020
# Modifying a List inside a Function 

def passengers(not_checked_in, checked_in):
    while not_checked_in:
        current_passenger = not_checked_in.pop()

        print("Checking in passenger: " + current_passenger.title() + '.')
        checked_in.append(current_passenger)

def show_checked_in_passengers(checked_in):
    print("\nThe following passengers have been checked in:" )
    for passengers in checked_in:
        print(passengers.title())

not_checked_in = ['donkey Kong', 'diddy kong', 'dixie kong', 'cranky kong']
checked_in = []

passengers(not_checked_in, checked_in)
show_checked_in_passengers(checked_in)

