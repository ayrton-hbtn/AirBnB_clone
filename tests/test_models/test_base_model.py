#!/usr/bin/python3
"""
    base_model tester
    module
    return: nothing
"""
import unittest
from models.base_model import BaseModel
import pep8


class Tester(unittest.TestCase):
    """ Test class """
    def test_docstring(self):
        """ Test doc strings """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)

    def test_default(self):
        i = BaseModel()
        self.assertEqual(type(i), BaseModel)

    def test_str(self):
        """ Test output of str method """
        i = BaseModel()
        string = f"[{type(i).__name__}] ({i.id}) {i.__dict__}"
        self.assertEqual(string, str(i))

    def test_to_dict(self):
        model = BaseModel()
        model.name = "My First Model"
        model.my_number = 89
        model_dict = model.to_dict()
        keys = ["id", "name", "my_number", "created_at",
                "updated_at", "__class__"]
        self.assertCountEqual(model_dict.keys(), keys)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["name"], "My First Model")
        self.assertEqual(model_dict["my_number"], 89)

    def test_pep8(self):
        """Test that file is PEP8 compliant """
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors,
                         0, "Found code style errors and warnings.")
