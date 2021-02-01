# TESTING QUESTION SEVEN


import unittest
from seven import occurence_count


#Here Is where I Perform the Unit Tests for question 7
import unittest

class Testseven(unittest.TestCase):
    def test_Occurence_count(self):
        a = "Data Structures"
        b = a.count("u")
        self.assertEqual(b, 2)

    def test_Occurence_again(self):
        c = "Data Structures"
        d = c.count("a")
        self.assertEqual(d, 2)


#this is to enable us to run the test from this file, without calling it on git
if __name__ == '__main__':
    unittest.main()

