#!/usr/bin/python3
"""
    
    module
    return: nothing
"""
from models.base_model import BaseModel

class State(BaseModel):
    ''' state '''
    def __init__(self, *args, **kwargs):
        self.name = ""
        super().__init__(self, **kwargs)