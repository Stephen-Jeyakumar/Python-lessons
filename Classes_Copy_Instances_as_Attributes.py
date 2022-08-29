# Classes
# 11-20-2020
# Copy of Making Instances As Attributes


# The same code as Making Instances as Attributes. Deleting some things to make it work butter.



# Same code as last time. Adding a new class called screen to tidy things up a bit. Thats all.

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




class Screen():
    def __init__(self, screen_resolution = '1280 x 800'):
        self.screen_resolution = screen_resolution

    def Describe_screen(self):
        print("\nKong Wood Industries proudly presents you with the latest invention of all times.... BIRCH BARK!! It also has a  " + self.screen_resolution + "  sized screen!")
    
       


class Kindle_Fire(Ereader):
    def __init__(self, make, model, backlight, battery, screen_type):

        super().__init__(make, model, backlight, battery, screen_type)

        self.Fire_screen = Screen()

           






