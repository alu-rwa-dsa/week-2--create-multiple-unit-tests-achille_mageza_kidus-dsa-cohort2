# TESTING QUESTION TEN

#here I import the modules and also import the function 
import unittest
from ten import this_pattern


#here I do the test for the function
class TestTen(unittest.TestCase):

    def test_pattern_one(self):
        var = this_pattern(2)
        self.assertEqual(var, [1, 2, 2])

    def test_pattern_two(self):
        variable = this_pattern(5)
        self.assertEqual(variable, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])



#this is to enable us to run the test from this file, without calling it on git
if __name__ == '__main__':
    unittest.main()


