""" Tests for password_checker.py """
import unittest
from password_checker import password_check


class TestPasswordCheck(unittest.TestCase):
    """ Test password_checker(*args) """

    def test_with_valid_password(self):
        """ Tests function prints out only passwords that match criteria. """
        pass

    def test_for_a_lower_alpha(self):
        """ Test for at least 1 lowercase character [a-z] in each password. """
        pass
    
    def test_for_an_upper_alpha(self):
        """ Test for at least 1 uppercase character [A-Z] in each password. """
        pass

    def test_for_a_numeric_char(self):
        """ Test for at least 1 numeric character [0-9] in each password. """
        pass

    def test_for_min_len(self):
        """ Test passwords for minimum length of 6 characters. """
        pass

    def test_for_max_len(self):
        """ Test passwords for maximum length of 12 characters. """
        pass

    def test_for_an_accepteted_symbolic_char(self):
        """ Test for at least 1 accepted symbolic character from [$#@] """
        pass

    def test_with_invalid_input(self):
        """ Tests handling of invalid input/invalid passwords """
        pass


