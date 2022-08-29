# Dictionaries
# 10-26-2020
# Using Dictionaries In Lists


Runt = {'Name': 'Runt',
        'Age': "Undefined",
        'Eye Color': 'Blue? idk',
        'Hair Color': 'Black',
}

Pebble = {'Name': "Pebble",
        "Age": 'Undefined',
        "Eye Color": "Purple",
        "Hair Color": 'Blue',
}

Stump = { 'Name': 'Stump',
        "Age": "Undefiend",
        "Eye Color": "Black? idk",
        "Hair Color": "Black",
}


characters = [Runt, Pebble, Stump]

for character in characters:
    print(character)



stock_items = []

for blue_pen in range(0,50):
    new_blue_pen = { 'Color': "Blue", 'Type': 'Ballpoint', 'Price': "$2.00"}
    stock_items.append(new_blue_pen)

for blue_pen in stock_items[0:5]:
    if blue_pen['Price'] == '$2.00':
        blue_pen['Price'] = '$1.00'

for blue_pen in stock_items[0:5]:
    print(blue_pen)


