#!/usr/bin/python3
'''Amenity class, inherits from BaseModel
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Creates instance of Amenity with an empty
    string as name, and inherits instantiation method
    from BaseModel
    '''
    def __init__(self, *args, **kwargs):
        self.name = ""
        super().__init__(self, **kwargs)