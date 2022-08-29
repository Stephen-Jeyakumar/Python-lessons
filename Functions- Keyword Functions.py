# Functions
# 11-3-2020
# Keyword Functions
book_name = input("What is the name of your current book?")
author_name = input("Who is the author of your current boook?")



def book_description(book_name, author_name):
    print("The name of your current book is " + book_name.title() + ".")
    print("The author of your current book is " + author_name.title() + '.')

book_description(book_name, author_name)