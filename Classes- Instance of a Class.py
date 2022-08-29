# Classes
# 11-12-2020
# Instance of a Class

# Just adding the arguments diddy kong, 2 bananas, and banana industries to the same code 
# for all of the 'class' lessons so far.

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



my_book = Book("diddy kong", '2 bananas', 'banana industries')