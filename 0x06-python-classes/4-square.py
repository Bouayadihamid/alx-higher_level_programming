#!/usr/bin/python3
"""Square."""


class Square:
    """A square."""

    def __init__(self, size=0):
        """Hamid.

        Args:
            size: The length.
        """
        self.size = size

    @property
    def size(self):
        """Property for the length.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Square Area.

        Return:
            Square size
        """
        return self.__size ** 2
