#!/bin/usr/python3
"""
Rectangle class.
"""
from base import Base

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
        self.__width = width
    @height.setter
    def height(self, height):
        """Height setter"""
        self.__height = height
    @x.setter
    def x(self, x):
        """X setter"""
        self.__x = x
    @y.setter
    def y(self, y):
        """Y setter"""
        self.__y = y

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
