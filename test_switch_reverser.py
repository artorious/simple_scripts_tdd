#!/usr/bin/env python3
""" Tests for switch_reverser.py """

import unittest
from switch_reverser import switch_reverser


class TestSwitchReverser(unittest.TestCase):
    """ Test cases for switch_reverser() """

    def test_with_list_of_integers(self):
        """ Test that a list of only integers is reversed. """
        self.assertListEqual([5, 4, 3, 2, 1], switch_reverser([1, 2, 3, 4, 5]))

    def test_with_list_of_words_only(self):
        """ Test that a list of words only is converted to uppercase. """
        self.assertListEqual(
            ['ABC', 'CDE', 'EFG'],
            switch_reverser(['abc', 'cde', 'efg'])
        )
        self.assertListEqual(
            ['1ABC', 'CDE', 'EFG'],
            switch_reverser(['1abc', 'cde', 'efg'])
        )

    def test_with_set_tuple(self):
        """ Test handling of sets and tuples """
        self.assertListEqual([5, 4, 3, 2, 1], switch_reverser((1, 2, 3, 4, 5)))
        self.assertListEqual([5, 4, 3, 2, 1], switch_reverser({1, 2, 3, 4, 5}))

    def test_with_mixed_datatypes(self):
        """ Test with a list items of different datatypes """
        self.assertListEqual(
            ['abc', 'def', 1],
            switch_reverser(['abc', 'def', 1])
        )
        self.assertListEqual(
            [1, 2, [3, 4], 5],
            switch_reverser([1, 2, [3, 4], 5])
        )

    def test_invalid_input(self):
        """ Test handling of strings, integers, floats, dicts """

        self.assertEqual(
            switch_reverser('abc'),
            'Expected list, set, or tuple'
        )
        self.assertEqual(switch_reverser(1), 'Expected list, set, or tuple')
        self.assertEqual(
            switch_reverser({'alpha': 'abc'}),
            'Expected list, set, or tuple'
        )
        self.assertEqual(switch_reverser(1.9), 'Expected list, set, or tuple')


if __name__ == '__main__':
    unittest.main()

