# Classes
# 11-12-2020
# Calling a Method

# Adding a new Function that lists the book title, price, and publisher in a library.
# Still The same code as the previous 'class' lessons. 

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
    
    def Ebook_reader(self):
        print("Library: " + self.name.title() + ", " + self.price.title() + ", " + self.publisher.title() + '.')


my_book = Book("OOH OOH EEEH SKEEK YAAAH OOOOOOOK", '21 bananas', 'banana industries')

# Printing out stuff.

print("I am currently reading the book called " + my_book.name.title() + ".")

print("This book cost me " + my_book.price.title() + '.') 

print('This book was published by ' + my_book.publisher.title() + '.' )

my_book.Ebook()

# Printing out new function

my_book.Ebook_reader()