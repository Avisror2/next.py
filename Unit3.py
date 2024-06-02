# Custom exception classes
class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg, char, index):
        self._arg = arg
        self._char = char
        self._index = index

    def __str__(self):
        return "The username contains an illegal character \"{}\" at index {}".format(self._char, self._index)

    def get_arg(self):
        return self._arg


class UsernameTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Username is too short"

    def get_arg(self):
        return self._arg


class UsernameTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Username is too long"

    def get_arg(self):
        return self._arg


class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Password is missing a character"

    def get_arg(self):
        return self._arg


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __init__(self, arg):
        PasswordMissingCharacter.__init__(self, arg)

    def __str__(self):
        return PasswordMissingCharacter.__str__(self) + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __init__(self, arg):
        PasswordMissingCharacter.__init__(self, arg)

    def __str__(self):
        return PasswordMissingCharacter.__str__(self) + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    def __init__(self, arg):
        PasswordMissingCharacter.__init__(self, arg)

    def __str__(self):
        return PasswordMissingCharacter.__str__(self) + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __init__(self, arg):
        PasswordMissingCharacter.__init__(self, arg)

    def __str__(self):
        return PasswordMissingCharacter.__str__(self) + " (Special)"


class PasswordTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Password is too short"

    def get_arg(self):
        return self._arg


class PasswordTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Password is too long"

    def get_arg(self):
        return self._arg


# Checks for a valid input of username and password- input length,  necessary english/special characters and numbers
def check_input(username, password):
    valid_username = True  # boolean representing a valid input for username defaulted as True
    valid_password = True  # boolean representing a valid input for password defaulted as True

    # Username validation checks
    try:
        if len(username) < 3:  # Check if the username is too short
            raise UsernameTooShort(username)
            valid_username = False
        if len(username) > 16:  # Check if the username is too long
            raise UsernameTooLong(username)
            valid_username = False
        if not any(c.isalpha() for c in username):  # Check if the username contains english letters
            valid_username = False
        if not any(c.isdigit() for c in username):  # Check if the username contains numbers
            valid_username = False
        if username.find('_') == -1:  # Check if the username contains an underscore '_'
            valid_username = False
        # Check for illegal characters
        valid_characters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
        for index, char in enumerate(username):
            if char not in valid_characters:
                raise UsernameContainsIllegalCharacter(username, char, index)

        # Password validation checks
        if len(password) < 8:  # Check if the password is too short
            raise PasswordTooShort(password)
            valid_password = False
        if len(password) > 40:  # Check if the password is too long
            raise PasswordTooLong(password)
            valid_password = False
        if not any(c.isupper() for c in password):  # Check if the password contains an uppercase letter
            raise PasswordMissingUppercase(password)
            valid_password = False
        if not any(c.islower() for c in password):  # Check if the password contains a lowercase letter
            raise PasswordMissingLowercase(password)
            valid_password = False
        if not any(c.isdigit() for c in password):  # Check if the password contains numbers
            raise PasswordMissingDigit(password)
            valid_password = False
        if not any(not c.isalnum() for c in password):  # Check if the username contains a special character
            raise PasswordMissingSpecial(password)
            valid_password = False

        if valid_username and valid_password:
            print('OK')
    except Exception as e:
        print(e)
        return False

    return True


def main():
    username = input('Enter username ')
    password = input('Enter password ')
    while not check_input(username, password):
        username = input('Enter username ')
        password = input('Enter password ')

    """
    Test cases
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")
    """


if __name__ == '__main__':
    main()
