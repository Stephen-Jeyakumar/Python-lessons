# Miscellaneous
# 11-29-2020
# Testing Code 3

# Importing some Test thing that basically tests a function and stuf

import unittest

from Miscellaneous_Testing_Code import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('diddy', 'kong')
        self.assertEqual(formatted_name, 'Diddy Kong')

unittest.main()
