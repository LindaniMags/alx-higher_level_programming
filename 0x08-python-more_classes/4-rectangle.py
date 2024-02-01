#!/usr/bin/python3
"""Class Rectangle that defines a rectangle."""


class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """Class attributes.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter, setter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter, setter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area calculation."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Perimeter calculation."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """informal string representation of the object"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        shape = []
        for i in range(self.__height):
            [shape.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                shape.append("\n")
        return ("".join(shape))

    def __repr__(self):
        """string representation of object."""
        shape = "Rectangle(" + str(self.__width)
        shape += ", " + str(self.__height) + ")"
        return (shape)
