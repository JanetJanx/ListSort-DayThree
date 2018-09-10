#import test library
import unittest
#import list function from list sorting file for testing
from list_sorting import list_sort

class ListTest(unittest.TestCase):

    def test_list_sort(self):
        #tests for numbers and letters
        self.assertEqual(list_sort([1,6,5,0,'c','m']), {'odds': [1, 5], 'evens': [0, 6], 'chars': ['c', 'm']})

        #tests for numbers, letters and characters
        self.assertEqual(list_sort([4,9,7,8,'d','g','!']), {'evens': [4, 8], 'odds': [7, 9], 'chars': ['!', 'd', 'g']})

        #test for empty lists
        self.assertEqual(list_sort([]), {'evens': [], 'odds': [], 'chars': []})

    def test_list_sort_with_boolean_items(self):
        self.assertEqual(list_sort([4,9,7,8,False,True,'d','g','!']), {'evens': [4, 8], 'odds': [7, 9], 'chars': ['!', 'd', 'g']})
    
    def test_list_sort_with_non_lists(self):
        self.assertEqual(list_sort(2), "Not a List")

if __name__ == "__main__":
    unittest.main()
    