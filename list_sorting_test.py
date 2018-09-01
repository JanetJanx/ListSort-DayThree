#import test library
import unittest
#import list function from list sorting file for testing
from list_sorting import list_sort

class ListTest(unittest.TestCase):

    def test_list_sort(self):
        #tests for numbers and letters
        self.assertEquals(list_sort([1,6,5,0,'c','m']), {'odds': [1, 5], 'evens': [0, 6], 'chars': ['c', 'm']})

        #tests for numbers, letters and characters
        self.assertEquals(list_sort([4,9,7,8,'d','g','!']), {'evens': [4, 8], 'odds': [7, 9], 'chars': ['!', 'd', 'g']})

        #test for empty lists
        self.assertEquals(list_sort([]), {'evens': [], 'odds': [], 'chars': []})

if __name__ == "__main__":
    unittest.main()
    