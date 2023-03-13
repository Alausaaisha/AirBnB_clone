#!/usr/bin/pyhon3
"""this module contains class Review that inherits from BaseModel"""


from models.base_model import BaseModel


class Review(BaseModel):
    """class created"""

    text = ""
    user_id = ""
    place_id = ""
