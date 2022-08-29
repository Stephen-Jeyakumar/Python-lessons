# Classes
# 11-12-2020
# Accessing Attributes

# This code accesses the name and price of the book and prints it out. 
# It is still the same code for all the previous 'class' lessons so far. 

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



my_book = Book("OOH OOH EEEH SKEEK YAAAH OOOOOOOK", '21 bananas', 'banana industries')

# Printing out stuff.

print("I am currently reading the book called " + my_book.name.title() + ".")
print("This book cost me " + my_book.price.title() + '.') 
print('This book was published by ' + my_book.publisher.title() + '.' )