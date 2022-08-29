# Functions
# 11-8-2020
# Passing a List to a Function

# Example code for 'Importing a Module' 
# That's why the title is a different format

def books_available(*books):
    for book in books:
        books_in_stock = "The following book is available to buy: " + book.title() + '.'
        print(books_in_stock)

