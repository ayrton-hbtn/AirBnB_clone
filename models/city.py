#!/usr/bin/python3
'''City class, inherits from BaseModel
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''City with public class attributes state_id and name
    as empty strings, inherits instantiation from BaseModel
    '''
    state_id = ""
    name = ""
