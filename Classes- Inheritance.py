# Classes 
# 11-18-2020
# Inheritance


# Same code as last time, making a new class in this same code.
# Parent and Child classes Ereader is parent class. Child class gets all methods from parent
# Called 'Inheritance' lol.
class Ereader():
    def __init__ (self, make, model, backlight, battery, screen_type):
        self.make = make
        self.model = model 
        self.backlight = backlight
        self.battery = battery
        self.screen_type = screen_type
        self.library_count = 0

    def get_Ereader_name(self):
        long_name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery + ' - ' + self.screen_type
        return long_name.title()

    def read_library_count(self):
        print("You have " + str(self.library_count) + " books in your library.")

    def update_library_count(self, ebook_count):
        self.library_count = ebook_count

    def Increment_library_count(self, purchased_ebooks):
        self.library_count += purchased_ebooks




my_new_Ereader = Ereader('piece of wood', 'Kong Wood makers', 'no lights', 'no battery', 'no screen')
print(my_new_Ereader.get_Ereader_name())

my_new_Ereader.library_count = 50
my_new_Ereader.read_library_count()

my_new_Ereader.update_library_count(75)
my_new_Ereader.read_library_count()

my_new_Ereader.Increment_library_count(10)
my_new_Ereader.read_library_count()

class Kindle_Fire(Ereader):
    def __init__(self, make, model, backlight, battery, screen_type):
        super().__init__(make, model, backlight, battery, screen_type)
    

my_Kindle_Fire = Kindle_Fire('amazon', 'kindle fire', 'backlight', '512 hour battery life', 'blue LED screen')
print(my_Kindle_Fire.get_Ereader_name())