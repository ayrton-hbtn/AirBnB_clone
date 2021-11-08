#!/usr/bin/python3
'''
'''
import json
from models.base_model import BaseModel

class FileStorage:
    ''' File Storage '''
    def __init__(self):
        ''' init '''
        self.__file_path = "file.json"
        self.__objects = {}
    
    def all(self):
        ''' returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj
    
    def save(self):
        ''' serializes __objects to the JSON file '''
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        st = json.dumps(obj_dict)
        with open(self.__file_path, "w") as f:
            f.write(st)

    def reload(self):
        ''' deserializes the JSON file to __objects '''
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.loads(f.read())
                for key, value in obj_dict.items():
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
