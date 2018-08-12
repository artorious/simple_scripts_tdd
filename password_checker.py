""" A simple program that checks validity of password input by user. """
import re  

def password_check(passwords):
    """ Accepts a sequence of comma separated <passwords> and checks each 
        password for:
            + at least 1 letter between [a-z]
            + at least 1 number between [0-9]
            + at least 1 letter between [A-Z]
            + at least 1 character from [$#@]
            + minimum password length of 6 characters
            + maximum password least of 12 characters
        Prints out comma separated passwords that match the criteria. 
    """
    if isinstance(passwords, str):
        raw_passwords_list = passwords.split(',')
        passwords_list = []

        for potential_password in raw_passwords_list:
            invalid_password = True
            while invalid_password:
                if len(potential_password) < 6 or len(potential_password) > 12:
                    break
                elif not re.search(r'[a-z]', potential_password):
                    break
                elif not re.search(r'[A-Z]', potential_password):
                    break
                elif not re.search(r'[0-9]', potential_password):
                    break
                elif not re.search(r'[@#$]', potential_password):
                    break
                else:
                    passwords_list.append(potential_password)
                    invalid_password = False


        if passwords_list == []:
            return 'No valid password found'
        else:
            return ','.join(str(password) for password in passwords_list) 
    else:
        raise TypeError('Argument should be a string') 

