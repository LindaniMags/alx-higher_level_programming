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

    def area(self):
        """ the area value of the Rectangle instance"""
        return self.height*self.width
    
    def display(self):
        """
         prints in stdout the Rectangle instance with the character #
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
    
    def update(self, *args, **kwargs):
        """Updating Rectangle class.

        Args:
            *args: added args.
            1st arg: id
            2nd arg: width
            3rd arg: height
            4th arg: x
            5th arg: y
            **kwargs: keyworded args
        """
        if args and len(args) != 0:
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for k, val in kwargs.items():
                if k == "id":
                    if val is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val
                elif k == "width":
                    self.width = val
                elif k == "height":
                    self.height = val
                elif k == "x":
                    self.x = val
                elif k == "y":
                    self.y = val

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
