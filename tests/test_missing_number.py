#import test library
import unittest
#import list function from list sorting file for testing
from missing_numbers import missing_number

class TestMissingNumber(unittest.TestCase):

    def test_missing_number(self):
        self.assertEqual(missing_number([10,14,20]), [11, 12, 13, 15, 16, 17, 18, 19])
    
    def test_missing_number_for_empty_list(self):
        self.assertEqual(missing_number([]), [])
    
    def test_missing_number_unsorted_list(self):
        self.assertEqual(missing_number([13,10,5]), [6, 7, 8, 9, 11, 12])


if __name__ == "__main__":
    unittest.main()