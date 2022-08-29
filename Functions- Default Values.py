# Functions
# 11-4-2020
# Default Values

author_name = input("Who is the author of yer current book? Hmmmmmm?")
book_name =  input("What is the name of yer current book? Hmmmmmmm?")


def book_description(author_name, book_name):
    print(book_name.title() + " is the name of the current book you are reading.")
    print("An organism named " + author_name.title() + " is actually the author of book you are currently reading.")
book_description(author_name, book_name)