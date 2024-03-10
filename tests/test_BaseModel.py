#!/usr/bin/python3
"""Testing BaseModel class."""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Actual tests."""
    def setUp(self):
        self.b = BaseModel()
        self.b1 = BaseModel()

    def test_classes(self):
        self.assertIsNotNone(self.b.id)
        self.assertIsInstance(self.b.id, str)
        self.assertIsInstance(self.b.created_at, datetime)
        self.assertIsInstance(self.b.updated_at, datetime)
        self.assertNotEqual(self.b.id, self.b1.id)

    def test_attributes(self):
        attr = ["id", "created_at", "updated_at"]
        for attrib in attr:
            self.assertTrue(hasattr(self.b, attrib))

    def test_save(self):
        """Test save method of BaseModel."""
        old_updated_at = self.b.updated_at
        self.b.save()
        self.assertNotEqual(old_updated_at, self.b.updated_at)

    def test_to_dict(self):
        """Test to_dict method of BaseModel."""
        model_dict = self.b.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str(self):
        """Test str method of BaseModel."""
        self.assertEqual(str(self.b), "[BaseModel] ({}) {}".format(
            self.b.id, self.b.__dict__))

    def test_from_dict(self):
        """Test creating BaseModel from dictionary."""
        model_dict = {
            '__class__': 'BaseModel',
            'id': '123',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T00:00:00'
        }
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, '123')
        self.assertEqual(new_model.created_at, datetime(2023, 1, 1, 0, 0))
        self.assertEqual(new_model.updated_at, datetime(2023, 1, 1, 0, 0))

    def test_custom_attributes(self):
        """Test setting custom attributes."""
        self.b.name = "TestModel"
        self.assertEqual(self.b.name, "TestModel")

    def tearDown(self):
        del self.b
        del self.b1


if __name__ == "__main__":
    unittest.main()
