#!/usr/bin/python3
'''Amenity class, inherits from BaseModel
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Amenity with public class attribute name,
    inherits instantiation from BaseModel
    '''
    name = ""
