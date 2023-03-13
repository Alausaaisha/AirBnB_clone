#!/usr/bin/python3
"""This module contains a class Basemodel that defines all
common attributes/methods for other classes"""


import uuid
from datetime import datetime
from models import storage
timeformat = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """class created"""

    def __init__(self, *args, **kwargs):
        """method instantiates class and initializes with the
        attributes in the parameter"""

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            self.created_at = datetime.strptime(kwargs["created_at"],
                                                timeformat)
            self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                timeformat)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """this method overrides the inbuilt __str__ method"""

        return("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of
        __dict__ of the instance"""

        dicti = self.__dict__.copy()
        dicti["created_at"] = dicti["created_at"].isoformat()
        dicti["updated_at"] = dicti["updated_at"].isoformat()
        dicti["__class__"] = self.__class__.__name__
        return(dicti)
