#!/usr/bin/python3
"""
Defines the base class.
"""
import json

class Base:
    """Base class."""
    __nb_objects = 0
    def __init__(self, id=None):
        """Base class constructor"""
        if id is None:
            Base.__nb_objects+=1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        file_1 = cls.__name__ + ".json"
        with open(file_1, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
    
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                inst = cls(1, 1)
            else:
                inst = cls(1)
            inst.update(**dictionary)
            return inst

    def load_from_file(cls):
        """Returns a list of instances"""
        file_2 = str(cls.__name__) + ".json"
        try:
            with open(file_2) as f:
                dict_list = Base.from_json_string(f.read())
                return [cls.create(**o) for o in dict_list]
        except IOError:
            return []
