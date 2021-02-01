#testing question nine
from nine import difference


#Here Is where I Perform the Unit Tests
import unittest
class Testnine(unittest.TestCase):
    def test_difference1(self):
        list_A = [1,9,2,3,4,5]
        list_B = [1,2,3,4,5]

        self.assertEqual(difference(list_A, list_B), [9])


    def test_difference2(self):
        list_C = [5,1,2,3,4]
        list_D = [1,2,3,4]

        self.assertEqual(difference(list_C, list_D), [5])

#this is to enable us to run the test from this file, without calling it on git
if __name__ == '__main__':
    unittest.main()

