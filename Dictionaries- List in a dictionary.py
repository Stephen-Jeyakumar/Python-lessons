# Dictionaries 
# 10-28-2020
# List in a dictionary


car = {
    'type': 'Tesla',
    'Model':'S',
    "Extras": [ 'Inside TV (hopefully)', 'Touchscreen (i think)', "other kewl stuff (definately)"]
}

print('The car you ordered was a ' +car['type'] + ", model " +car['Model'] + ", that has some cool features such as:")
for extra in car['Extras']:
    print("\t" + extra)











