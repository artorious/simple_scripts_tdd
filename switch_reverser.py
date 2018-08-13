#!/usr/bin/env python3
""" Swap the order of items in a collection of data """


def switch_reverser(a_list):
    """ Swaps the order of items in the provided list

        Reverses the order if the list consist of integers alone.
        Converts the list items to uppercase if all items are words.
        Returns the modified list. If provided list does not match the above
        criteria, the same is returned as it is.
    """
    if isinstance(a_list, (list, tuple, set)):
        a_list = list(a_list)

        if set([type(item) for item in a_list]) == {int}:
            a_list = a_list[::-1]
        elif set([type(item) for item in a_list]) == {str}:
            a_list = [item.upper() for item in a_list]

        return a_list
    else:
        return 'Expected list, set, or tuple'

