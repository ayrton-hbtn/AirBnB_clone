#!/usr/bin/python3
"""
    base_model tester
    module
    return: nothing
"""
import unittest
from models import base_model

class Tester(unittest.TestCase):
    """ Test class """

    def test_doc_module(self):
        """ test for module documentation """
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_doc_class(self):
        """ test for class documentation """
        self.assertTrue(len(base_model.BaseModel.__doc__) > 0)

    def test_doc_save(self):
        """ test for method <save> documentation """
        self.assertTrue(len(base_model.BaseModel.save.__doc__) > 0)

    def test_doc_to_dict(self):
        """ test for method <to dict> documentation """
        self.assertTrue(len(base_model.BaseModel.to_dict.__doc__) > 0)
