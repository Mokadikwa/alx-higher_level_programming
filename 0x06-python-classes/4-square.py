#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """initialize a new square"""
        self.__size = size

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method to set it"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
