#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """Size setter"""
        self.width = size
        self.height = size

    def __str__(self):
        """ Overloading __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    def update(self, *args, **kwargs):
        """Updating Square class.

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
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1

        elif kwargs and len(kwargs) != 0:
            for k, val in kwargs.items():
                if k == "id":
                    if val is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = val
                elif k == "size":
                    self.size = val
                elif k == "x":
                    self.x = val
                elif k == "y":
                    self.y = val

    def to_dictionary(self):
        """Returns the dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
