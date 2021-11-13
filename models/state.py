#!/usr/bin/python3
'''State class, inherits from BaseModel
'''
from models.base_model import BaseModel


class State(BaseModel):
    '''State with single class attribute name as empty string,
    inherits instantiation from BaseModel
    '''
    name = ""
