# Functions
# 11-3-2020
# Positional Arguments
book_type = input("What is the name of the book you are reading?")
author_name = input("Who is the author of this book?")


def book_description(book_type, author_name):
    print("This book is " + book_type.title() + ".")
    print("The author of this book is "+ author_name.title() + '.')
book_description(book_type, author_name)