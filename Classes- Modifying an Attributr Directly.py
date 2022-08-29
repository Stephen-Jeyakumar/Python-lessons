# Classes
# 11-17-2020
# Modifying an attribute directly

# Same code as the previous Ereader classes.
# Just changing the amt. of books in library by saying my_new_Ereader.library_count = 50.

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


my_new_Ereader = Ereader('piece of wood', 'Kong Wood makers', 'no lights', 'no battery', 'no screen')
print(my_new_Ereader.get_Ereader_name())

my_new_Ereader.library_count = 50
my_new_Ereader.read_library_count()