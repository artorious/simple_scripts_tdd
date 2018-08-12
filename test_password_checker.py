""" Tests for password_checker.py """
import unittest
from password_checker import password_check


class TestPasswordCheck(unittest.TestCase):
    """ Test password_checker(*args) """

    def test_with_valid_password(self):
        """ Tests function prints out only passwords that match criteria. """
        self.assertEqual(
            password_check('Az09#@$,a F1#,2w3E*,2We3345'), 'Az09#@$'
        )
        self.assertEqual(
            password_check('Az09#@$,Ab1#xx,a F1#'), 'Az09#@$,Ab1#xx'
        )
        self.assertEqual(password_check(''), 'No valid password found')

    def test_for_a_lower_alpha(self):
        """ Test for at least 1 lowercase character [a-z] in each password. """
        self.assertEqual(password_check('Az09#@$,AZ09#@$'), 'Az09#@$')

    def test_for_an_upper_alpha(self):
        """ Test for at least 1 uppercase character [A-Z] in each password. """
        self.assertEqual(password_check('Az09#@$,az09#@$'), 'Az09#@$')

    def test_for_a_numeric_char(self):
        """ Test for at least 1 numeric character [0-9] in each password. """
        self.assertEqual(password_check('Az09#@$,az$$#@$'), 'Az09#@$')
        self.assertEqual(password_check('az$$#@$'), 'No valid password found')

    def test_for_min_len(self):
        """ Test passwords for minimum length of 6 characters. """
        self.assertEqual(password_check('Az09#,Az09@$'), 'Az09@$') 
        self.assertEqual(password_check('Az09#'), 'No valid password found') 

    def test_for_max_len(self):
        """ Test passwords for maximum length of 12 characters. """
        self.assertEqual(
            password_check('Az09@$#xxxxx,Az09@$#xxxxxyy'), 'Az09@$#xxxxx'
        ) 
        self.assertEqual(password_check('Az09@$#xxxxxyy'), 'No valid password found') 

    def test_for_an_accepteted_symbolic_char(self):
        """ Test for at least 1 accepted symbolic character from [$#@] """
        self.assertEqual(password_check('Az09*-^!,Az09@$#*^'), 'Az09@$#*^')


    def test_with_invalid_input(self):
        """ Tests handling of invalid input/invalid passwords """
        with self.assertRaises(TypeError) as context:
            password_check(1)
            self.assertEqual(
                'Argument should be a string',
                context.exception.message,
                'String inputs allowed only'
            )


