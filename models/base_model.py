#!/usr/bin/python3
'''BaseModel class, parent of all the other classes
in the program
'''

import uuid
from datetime import datetime
import models

class BaseModel:
    '''Creates instance of BaseModel; if a dictionary is passed, the method
    will set object attributes name, value from dictionary pair key, value
    (Ignores '__class__' key).
    Otherwise, it will assign a new id, creation time and update time, and save
    it to storage.
    '''
    def __init__(self, *args, **kwargs):
        if kwargs is not None and len(kwargs) >= 1:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f'))
                    continue
                setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        '''Updates object's attribute 'updated_at'
        and saves it to JSON file
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Creates a dictionary out of a custom class
        object and returns it
        '''
        obj = dict(self.__dict__)
        obj['__class__'] = type(self).__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
    
    def __str__(self):
        '''String format returned when class instance is called by
        print() method
        '''
        p = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return p