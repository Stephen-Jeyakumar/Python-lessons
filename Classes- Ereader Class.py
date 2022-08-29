# Classes 
# 11-15-2020
# Ereader Class 

# Making a new class called 'Ereader'

class Ereader():
    def __init__ (self, make, model, backlight, battery, screen_type):
        self.make = make
        self.model = model 
        self.backlight = backlight
        self.battery = battery
        self.screen_type = screen_type
    def get_Ereader_name(self):
        long_name = self.make + ' - ' + self.model + ' - ' + self.backlight + ' - ' + self.battery + ' - ' + self.screen_type
        return long_name.title()

my_new_Ereader = Ereader('piece of wood', 'Kong Wood makers', 'no lights', 'no battery', 'no screen')
print(my_new_Ereader.get_Ereader_name())
