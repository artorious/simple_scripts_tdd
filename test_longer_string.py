#!/usr/bin/env python3
""" Tests for longer_string.py """
import unittest
from longer_string import longer_string


class TestLongerString(unittest.TestCase):
    """ Test cases for longer_string() """

    def test_invalid_input(self):
        """ Tests both arguments are strings """
        with self.assertRaises(TypeError):
            longer_string('art', 1)
            self.assertEqual('Expected  strings')
        
        with self.assertRaises(TypeError):
            longer_string(11, 1)
            self.assertEqual('Expected  strings')

    def test_different_lengths(self):
        """ Test function prints the longer of the two strings provided """
        self.assertEqual(longer_string('art', 'arthur'), 'arthur')

    def test_same_lengths(self):
        """ Test function prints both strings if they are of the same length
        """
        self.assertEqual(longer_string('arthur', 'ngondo'), 'arthur\nngondo')

if __name__ == '__main__':
    unittest.main()
