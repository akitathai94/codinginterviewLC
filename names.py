from name_function import get_formatted_name
import unittest

class NameTestCase(unittest.TestCase):
    """ Tests for 'name_function.py'. """
    def test_first_last_name(self):
        """Do names like 'Thai Truong' works? """
        formatted_name = get_formatted_name('thai', 'truong')
        self.assertEqual(formatted_name, 'Thai Truong')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()