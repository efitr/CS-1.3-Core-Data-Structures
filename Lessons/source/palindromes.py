#!python

import string
from math import ceil, floor
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

def clean(palindrome):
    palindrome = palindrome.lower()
    for letter in palindrome:
        if ord(letter) < 97 or ord(letter) > 122:
            palindrome = palindrome.replace(letter, "")
    return palindrome

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    text = clean(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    if text == '':
        return True

    if len(text) == 1:
        return True

    middle_position = ceil(len(text)/2)
    position = 0
    last_position = len(text)-1

    while text[position] == text[last_position]:
        if position == middle_position:
            return True
        position += 1
        last_position -= 1
    return False

def is_palindrome_recursive(text, first_index=None, last_index=None):
    # TODO: implement the is_palindrome function recursively here
    # Cleaning the text, only happens once
    if first_index is None and last_index is None:
        if text == '':
            return True
        if len(text) == 1:
            return True

        # left and right both must be indexes
        first_index = 0
        last_index = len(text)-1

    # len = 7, middle = 4
    middle_position = ceil(len(text)/2)

    if text[first_index] is text[last_index]:
        
        if last_index == middle_position:
            return True
        return is_palindrome_recursive(text, first_index=first_index+1, last_index=last_index-1)

    return False

     # could be 
    
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    # main()
    is_palindrome_recursive("racecar")
