#import test library
import unittest
#import list function from list sorting file for testing
from list_sorting import list_sort

class ListTest(unittest.TestCase):

    def test_list_sort(self):
        self.assertEquals(list_sort([1,6,5,0,'c','m']), {'odds': [1, 5], 'evens': [0, 6], 'chars': ['c', 'm']})

if __name__ == "__main__":
    unittest.main()