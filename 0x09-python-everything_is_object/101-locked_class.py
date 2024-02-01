#!/usr/bin/python3
"""Class withouth attributes"""

class LockedClass:
    """Prevents user from creating new attributes"""

    __slots__ = ["first_name"]
