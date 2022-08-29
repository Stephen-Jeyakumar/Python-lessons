# Classes
# 11-22-2020
# Importing a Whole Module

# Almost the same code as the multiple classes from a module program, just editing a few things.

import Classes_Copy_Instances_as_Attributes

my_bw_ereader = Classes_Copy_Instances_as_Attributes.Ereader('amazon', 'paperweight', 'adjustable backlight', 'battery - 10 months', '790.9 dpi')

my_color_ereader = Classes_Copy_Instances_as_Attributes.Kindle_Fire('amazon', 'kindle fire', 'adjustable backlight', 'battery - 20 months', 'color screen  1200 x 800')

print(my_bw_ereader.get_Ereader_name())

print(my_color_ereader.get_Ereader_name())