#!/usr/bin/python3
"""Module containing Base class"""
import json


class Base:
    """Base class itself"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base class instance"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns JSONstring representation of list_dictionaries"""

        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation of list_objs to file"""

        filename = cls.__name__ + ".json"
        towrite = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                jdict = json.loads(cls.to_json_string(item))
                towrite.append(jdict)

        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(towrite, f)

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string
        representation json_string"""

        if len(json_string) == 0 or json_string is None:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance withh all attributes already set"""

        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            dummy = Rectangle(1, 2)
        if cls.__name__ == "Square":
            dummy = Square(1)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + ".json"

        with open(filename, 'r', encoding="utf-8") as f:
            readfromfile = cls.from_json_string(f.read())

        instances = []
        for item in readfromfile:
            temp = cls.create(**item)
            instances.append(temp)

        return instances
