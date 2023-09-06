#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    :param first_name: The first name.
    :type first_name: str
    :param last_name: The last name (optional).
    :type last_name: str
    :raises TypeError: If `first_name` is not a string or if both `first_name` and `last_name` are not provided.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not first_name and not last_name:
        raise TypeError("At least one name must be provided.")
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
