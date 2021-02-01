# TESTING QUESTION EIGHT

import unittest
from eight import merge_list


#Here Is where I Perform the Unit Tests for question 8
import unittest

class TestEight(unittest.TestCase):
    def test_mergeList(self):
        list1 = [[1,2,3,4],[2,3,4,5],[4,5,6,7],[7,8,9,10]]
        List2 = merge_list(list1)

        self.assertEqual(List2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


#this is to enable us to run the test from this file, without calling it on git
if __name__ == '__main__':
    unittest.main()

