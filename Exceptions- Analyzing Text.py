# Exceptions
# 11-27-2020
# Analyzing Text

filename = 'Runt.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    message = print("Sorry, the file known as " + filename + " cannot be found in the whole world")
    print(message)
else:
    words = contents.split()
    number_of_words = len(words)
    print("The file known as " + filename + ' has aboutishness ' + str(number_of_words) + ' words.')
