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
