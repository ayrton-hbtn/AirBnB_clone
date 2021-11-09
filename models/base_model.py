#!/usr/bin/python3
'''
'''

import uuid
from datetime import datetime
import models

class BaseModel:
    ''''''
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
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        obj = dict(self.__dict__)
        obj['__class__'] = type(self).__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
    
    def __str__(self):
        p = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return p

    def update(self):
        ''' set update time '''
        self.updated_at = datetime.now()
