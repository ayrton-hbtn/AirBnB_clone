#!/usr/bin/python3
'''User class, inherits from BaseModel
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Creates a new instance of User with attributes email,
    password, first_name and last_name as empty strings.
    Inherits instantiation from BaseModel
    '''
    def __init__(self, *args, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(self, *args, **kwargs)
