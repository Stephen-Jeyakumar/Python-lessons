# Functions
# 11-9-2020
# Arbitrary Argument 2

def create_passenger(*requests):
    print("This passenger has requested: ")
    for request in requests:
        print("- " + request)



create_passenger('seat number 1', 'area 1', 'pre-ordered meals')


