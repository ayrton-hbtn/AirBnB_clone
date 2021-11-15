#!/usr/bin/python3
'''File Storage Class, to do JSON
serialization/deserialization
'''
import json
from models.engine import classes


class FileStorage:
    ''' File Storage '''
    __file_path = "file.json"
    __objects = {}

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
                    class_name = key.split(".")[0]
                    self.__objects[key] = classes[class_name](**value)
        except FileNotFoundError:
            pass

    def delete(self, key=""):
        """Deletes an instance """
        if key in self.__objects:
            del self.__objects[key]
            self.save()
