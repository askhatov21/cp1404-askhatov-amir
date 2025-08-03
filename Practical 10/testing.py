"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from Practical_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def format_phrase_as_sentence(phrase):
    """
      Format a phrase as a sentence with capital letter and single full stop.
    >>> format_phrase_as_sentence("hello")
    'Hello.'
    >>> format_phrase_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase_as_sentence("already ended.")
    'Already ended.'
    """
    # Strip leading/trailing spaces, capitalize first letter, and ensure one period at the end
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].upper() + phrase[1:]
def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"




    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car("TestCar")
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Test Car's default odometer
    default_car = Car("DefaultCar")
    assert default_car.fuel == 0, "Car does not set default fuel correctly"

    # Test Car's custom fuel
    fuel_car = Car("FuelCar", fuel=10)
    assert fuel_car.fuel == 10, "Car does not set custom fuel correctly"




run_tests()

doctest.testmod()