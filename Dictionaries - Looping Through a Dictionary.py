# Dictionaries 
# 10-23-2020
# Looping through a Dictionary

birthdays = {
    'steve': 'january',
    'runt': 'febuary',
    'pebble': 'december',
    'breeze': 'july',
    'Eebuzz': 'Kinlertiz' ,
}

print(birthdays)

for key, value in birthdays.items():
    print("\n" + key.title() + "'s birthday is:")
    print(value.title())