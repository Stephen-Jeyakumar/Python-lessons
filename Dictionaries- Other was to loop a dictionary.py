# Dictionaries
# 10-23-2020
# Other ways to loop a dictionary

birthdays = {
    'steve': 'january',
    'runt': 'febuary',
    'pebble': 'december',
    'breeze': 'july',
    'Eebuzz': 'Kinlertiz' ,
}

for name in birthdays.keys():   
    print(name.title())

for months in birthdays.values():
    print(months.title())
    
for months in set(birthdays.values()):
    print(months.title())