#!/usr/bin/python3
'''
'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    '''
    def __init__(self, *args, **kwargs):
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(self, **kwargs)