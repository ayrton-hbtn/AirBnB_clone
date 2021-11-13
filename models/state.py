#!/usr/bin/python3
'''State class, inherits from BaseModel
'''
from models.base_model import BaseModel


class State(BaseModel):
    '''Creates a new instance of State with single
    attribute name as empty string, inherits instantiation
    from BaseModel
    '''
    def __init__(self, *args, **kwargs):
        self.name = ""
        super().__init__(self, **kwargs)
