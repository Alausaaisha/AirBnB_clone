#!/usr/bin/python3
"""This module contains a class Basemodel that defines all
common attributes/methods for other classes"""


import uuid
from datetime import datetime
timeformat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """class created"""

    def __init__(self, *args, **kwargs):
        """method instantiates class and initializes with the
        attributes in the parameter"""

        if kwargs:
            for key, value in kwargs.items():
                if key !=  "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs["created_at"], timeformat)
            self.updated_at = datetime.strptime(kwargs["updated_at"], timeformat)
        else:
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

        dicti = self.__dict__.copy()
        dicti["created_at"] = datetime.now().isoformat()
        dicti["updated_at"] = datetime.now().isoformat()
        dicti["__class__"] = self.__class__.__name__.copy()
        return(dicti)
