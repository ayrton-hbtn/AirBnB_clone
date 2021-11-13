#!/usr/bin/python3
'''Review class, inherits from BaseModel
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Creates an instance of Review, inherits
    instantiation from BaseModel
    '''
    def __init__(self, *args, **kwargs):
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(self, **kwargs)
