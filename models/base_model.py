#!/usr/bin/python3
"""This module contains a class Basemodel that defines all
common attributes/methods for other classes"""


import uuid
from datetime import datetime


class BaseModel:
    """class created"""

    def __init__(self):
        """method instantiates class and initializes with the
        attributes in the parameter"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        

    def __str__(self):
        """this method overrides the inbuilt __str__ method"""

        return("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""

        new_time = self.updated_at = datetime.now().isoformat()
        return(new_time)

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""

        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        dicti = self.__dict__
        dicti["__class__"] = self.__class__.__name__
        return(dicti)
