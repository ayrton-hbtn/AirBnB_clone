#!/usr/bin/python3
"""
    file_storage tester
    module
    return: nothing
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
import pep8


class Tester(unittest.TestCase):
    """ Test FileStorage class """
    def test_docstring(self):
        """ Test class methods docstrings """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.delete.__doc__)

    def test_isinstance(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_all(self):
        obj_dict = FileStorage().all()
        self.assertEqual(type(obj_dict), dict)

    def test_new(self):
        model = BaseModel()
        FileStorage().new(model)
        obj_key = "BaseModel." + model.id
        dict_obj = FileStorage().all()
        self.assertIn(obj_key, dict_obj.keys())
