#!/usr/bin/python3
'''Review class, inherits from BaseModel
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Review with public class attributes place_id, user_id
    and text, inherits instantiation from BaseModel
    '''
    place_id = ""
    user_id = ""
    text = ""
