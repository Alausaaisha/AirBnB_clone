#!/usr/bin/python3
"""this module contains serialization and deserialization of object"""


import json


class FileStorage:
    """this class serializes instances to a JSON file and deserializes
    JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """this method returns the dictionary __objects"""

        return(self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = obj.__class__.__name__ + "." + obj.id

        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        new_obj = {}
        for key, value in self.__objects.items():
            new_obj[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding="UTF8") as f:
            json.dump(new_obj, f, indent=2)

    def reload(self):
        """deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)"""

        from models.base_model import BaseModel
        from models.user import User

        try:
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    if value["__class__"] == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    elif value["__class__"] == "User":
                        self.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
