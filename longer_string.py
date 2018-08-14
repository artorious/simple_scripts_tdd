#!/usr/bin/env python3
""" Find the longer string """


def longer_string(string1, string2):
    """ Accepts two strings as input

        Prints the string with the maximum length on the console.
        If the two strings have the same length, prints eack string on it's
        own line
    """
    if isinstance(string1, str) and isinstance(string2, str):
        if len(string1) == len(string2):
            output_str = '{0}\n{1}'.format(string1, string2)
        elif len(string1) > len(string2):
            output_str = '{}'.format(string1)
        else:
            output_str = '{}'.format(string2)

        return output_str
    else:
        raise TypeError('Expected strings')


if __name__ == '__main__':
    string1 = input('Enter the first string: ')
    string2 = input('Enter the second string to compare: ')
    print(longer_string(string1, string2))

