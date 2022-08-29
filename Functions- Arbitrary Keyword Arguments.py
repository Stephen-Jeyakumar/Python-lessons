# Functions
# 11-10-2020
# Arbitrary Keyword Arguments

def seat_profile(first, last, **passenger_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in passenger_info.items():
        profile[key] = value
    return profile

passenger_profile = seat_profile('diddy', 'kong', seat_number = 'monkey 4', breakfast_order = 'banana')

print(passenger_profile)

