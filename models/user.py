#!/usr/bin/python3
"""this module contains class User that inherits from BaseModel"""


from models.base_model import BaseModel


class User(BaseModel):
    """class defined"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
