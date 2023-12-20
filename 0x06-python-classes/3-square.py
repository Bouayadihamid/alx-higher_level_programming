#!/usr/bin/python3
"""Square"""



class Square:
    """A square."""

    def __init__(self, size=0):
        """Hamid.

        Args:
            size: The length of a side of the square.

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
    def area(self):
        """Square Area.

        Returns:
            The square size.
        """
        return self.__size ** 2
