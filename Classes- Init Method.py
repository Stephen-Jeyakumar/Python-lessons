# Classes
# 11-12-2020
# Init Method

# Just Tony explaining about this hole thing.

class Book():
    def  __init__(self, name, price, publisher):
        self.name = name
        self.price = price
        self.publisher = publisher
        
    def hardback(self):
        print(self.name.title() + " is a hardback book.")

    def softback(self):
        print(self.name.title() + " is a softback book.")

    def Ebook(self):
        print(self.name.title() + " is an E-book.")
