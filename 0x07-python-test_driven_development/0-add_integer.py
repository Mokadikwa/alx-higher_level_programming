#!/usr/bin/python3
<<<<<<< HEAD
"""
Function add_integer(a, b=98) adds 2 integers.
Parameters: a (int or float), b (int or float, optional).
Returns int: sum of a and b. Raises TypeError if a or b is not an integer or float.
Raises ValueError if a or b is NaN."""
=======
"""Function add_integer(a, b=98) adds 2 integers.
 Parameters: a (int or float), b (int or float, optional).
Returns int: sum of a and b. Raises TypeError if a or b is not an integer or float.
 Raises ValueError if a or b is NaN."""

>>>>>>> 449350a969ddec876e9f03f253a36aaa3c17b5dd

def is_nan(value):
    return value != value

<<<<<<< HEAD
def add_integer(a, b=98):
    """
    add 2 integers or floats
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    if is_nan(a) or is_nan(b):
        raise ValueError("cannot convert float NaN to integer")

    return (int(a) + int(b))
=======

def add_integer(a, b=98):
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
>>>>>>> 449350a969ddec876e9f03f253a36aaa3c17b5dd
