# Classes
# 11-22-2020
# Multiple Classes From A Module

from Classes_Copy_Instances_as_Attributes import Ereader, Kindle_Fire

my_bw_ereader = Ereader('amazon', 'paperweight', 'adjustable backlight', 'battery - 10 months', '790.9 dpi')

my_color_ereader = Kindle_Fire('amazon', 'kindle fire', 'adjustable backlight', 'battery - 20 months', 'color screen  1200 x 800')

print(my_bw_ereader.get_Ereader_name())

print(my_color_ereader.get_Ereader_name())
