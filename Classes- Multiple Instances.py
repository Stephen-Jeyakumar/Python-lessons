# Classes 
# 11-14-2020
# Multiple Instances

# Adding another variable for another book called 'your_book'
# Same code as the previous 'class' lessons

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
your_book = Book("AAH AAH MEE BANANA OOOOOK MONKEEE SKEEEK OOOOOOH", "30 bananas", "banana industries")

# Printing out stuff.

print("I am currently reading the book called " + my_book.name.title() + ".")

print("This book cost me " + my_book.price.title() + '.') 

print('This book was published by ' + my_book.publisher.title() + '.' )

my_book.Ebook()

# Printing out new function

my_book.Ebook_reader()
your_book.softback()