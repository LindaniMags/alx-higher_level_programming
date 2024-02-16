#!/usr/bin/python3
"""
Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """Define Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width
    @property
    def height(self):
        """Height getter"""
        return self.__height
    @property
    def x(self):
        """X getter"""
        return self.__x
    @property
    def y(self):
        """Y getter"""
        return self.__y
    
    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
    @height.setter
    def height(self, height):
        """Height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
    @x.setter
    def x(self, x):
        """X setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
    @y.setter
    def y(self, y):
        """Y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
