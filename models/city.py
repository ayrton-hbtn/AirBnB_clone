#!/usr/bin/python3
'''City class, inherits from BaseModel
'''
from models.base_model import BaseModel


class City(BaseModel):
    '''Creates a new instance of City with strings state_id
    and name empty, inherits instantiation from BaseModel
    '''
    def __init__(self, *args, **kwargs):
        self.state_id = ""
        self.name = ""
        super().__init__(self, **kwargs)