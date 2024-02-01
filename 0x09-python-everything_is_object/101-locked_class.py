#!/usr/bin/python3

"""Class withouth attributes."""

class LockedClass:

    """
    Prevents user from creating new attributes.

    Attributes:
        first-name: First name string.
    """

    __slots__ = ["first_name"]
