# Functions
# 11-10-2020
# Using Positional and Arbitrary Arguments together

def assign_seat(seat, *requests):
    print("\n Assign seat number " + str(seat) + ', the following passenger requests.')
    for request in requests:
        print("-" +  request)


assign_seat(79, 'window seat')