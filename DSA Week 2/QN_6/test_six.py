# TESTING QUESTION SIX


import unittest
from six import one_space
import re


#Here Is where I Perform the Unit Tests
import unittest

class Testsix(unittest.TestCase):
    def test_One_space(self):
        a = "I     am      a    student."
        b = re.sub("\s\s+" , " ", a)
        self.assertEqual(b, "I am a student.")

    def test_again(self):
        x = "Good         Day!"
        y = re.sub("\s\s+" , " ", x)
        self.assertEqual(y, "Good Day!")


if __name__ == '__main__':
    unittest.main()


