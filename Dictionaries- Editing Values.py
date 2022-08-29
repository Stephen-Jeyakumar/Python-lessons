# Dictionaries
# 10-21-2020
# Editing Values

terms = {'integer': 'not a whole number'}

terms['integer'] = 'A whole number'

print(terms.get('integer'))

terms_2 = {'integer': 'not a whole number', 'zero': 'neither positive nor negative'}

del terms_2 ['integer']

print(terms_2)
