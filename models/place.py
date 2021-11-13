#!/usr/bin/python3
'''Place class, inherits from BaseModel
'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''Creates a new instance of Place, inherits
    instantiation from BaseModel
    '''
    def __init__(self, *args, **kwargs):
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = float(0)
        self.longitude = float(0)
        self.amenity_ids = []
        super().__init__(self, **kwargs)