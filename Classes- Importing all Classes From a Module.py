# Classes
# 11-22-2020
# Importing all Classes From a Module

# Practically the same code as Multiple Classes From a Module, but we are just changing one thing.
# Ignore the error its sad and is mean to me and is not nice and is not helpful in any way and is annoying...
from Classes_Copy_Instances_as_Attributes import *

my_bw_ereader = Ereader('amazon', 'paperweight', 'adjustable backlight', 'battery - 10 months', '790.9 dpi')

my_color_ereader = Kindle_Fire('amazon', 'kindle fire', 'adjustable backlight', 'battery - 20 months', 'color screen  1200 x 800')

print(my_bw_ereader.get_Ereader_name())

print(my_color_ereader.get_Ereader_name())