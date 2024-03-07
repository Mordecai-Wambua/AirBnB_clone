#!/usr/bin/env python3
"""Class to serializes instances to a JSON file and deserializes JSON file to instances."""

class FileStorage:
    """Serialization and deserialization of instances to and from JSON file."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return the dictionary of __objects."""
        return self.__class__.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj: actual object
        """
        pass

    def save(self):
        """Serializes __objects to the JSON file."""
        pass

    def reload(self):
        """Deserializes the JSON file to __objects."""
        pass
