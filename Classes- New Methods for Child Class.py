# Classes
# 11-18-2020
# New Child Class Methods

# Same code as last time, adding new methods to child class.

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
print(my_new_Ereader.get_Ereader_name() + '\n')

my_new_Ereader.library_count = 50
my_new_Ereader.read_library_count()

my_new_Ereader.update_library_count(75)
my_new_Ereader.read_library_count()

my_new_Ereader.Increment_library_count(10)
my_new_Ereader.read_library_count()

print('\n')

class Kindle_Fire(Ereader):
    def __init__(self, make, model, backlight, battery, screen_type, screen_resolution = '1280 x 800'):
        super().__init__(make, model, backlight, battery, screen_type)
        self.screen_resolution = screen_resolution
    def Describe_screen(self):
        print("Kong Wood Industries proudly presents you with the latest invention of all times.... BIRCH BARK!! It also has a  " + self.screen_resolution + "  sized screen!")


my_Kindle_Fire = Kindle_Fire('amazon', 'kindle fire', 'backlight', '512 hour battery life', 'blue LED screen')
print(my_Kindle_Fire.get_Ereader_name() + '\n')

my_Kindle_Fire.Describe_screen()
