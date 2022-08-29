# Exceptions
# 11-28-2020
# Multiple Files

# Same code as Analyzing Text, making some changes.
def word_count(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("Sorry, the file known as " + filename + " cannot be found in the whole world")
        
    else:
        words = contents.split()
        number_of_words = len(words)
        print("The file known as " + filename + ' has aboutishness ' + str(number_of_words) + ' words.')


filenames = ['Runt.txt', 'Banana.txt', 'Favorite_Animal.txt']

for filename in filenames:
    word_count(filename)