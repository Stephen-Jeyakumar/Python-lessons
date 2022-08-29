# Functions
# 11-5-2020
# Return a Dictionary

def build_book(name, author, publisher):
    book = { 'name' : name.title(),
            'author': author.title(),
            'publisher': publisher.title()

    }
    return book

my_book = build_book("diddy kONG", 'diddy KoNg', 'DoNkEy KoNg')
print(my_book)