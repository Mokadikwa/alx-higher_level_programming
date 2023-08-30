#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Represent a square."""
    def __init__(self, size=0, position=(0, 0)):
        """initialize a new square"""
        self.__size = size
        self.__position = (0, 0)

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

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 values")

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout with char '#'"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print('#' *self.size)

        if self.position[1] > 0:
            print('-' * self.position[1])
        else:
            print()
