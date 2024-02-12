#!/usr/bin/python3
"""Defines the base class."""


class Base:
    """
    Base class.

    Class Attributes:
        __nb_objects: Private class attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize Base class

        Args:
            id: Class id.
        """

        if id != None:
            self.id = id
        else:
            Base.__nb_objects+=1
            self.id = Base.__nb_objects
