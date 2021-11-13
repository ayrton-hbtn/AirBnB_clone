#!/usr/bin/python3
'''User class, inherits from BaseModel
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''User with public class attributes email, password,
    first_name and last_name as empty strings.
    Inherits instantiation from BaseModel
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
