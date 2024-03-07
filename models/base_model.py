#!/usr/bin/env python3
"""Define class BaseModel to be inherited by other classes."""
import uuid
import datetime


class BaseModel:
    """Define all common attributes/methods for other classes."""

    def __init__(self):
        """Initialize attributes."""
        self.id = uuid.uuid4().hex
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """Update the attribute update_at with the current datetime."""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values."""
        new = self.__dict__
        new['__class__'] = self.__class__.__name__
        new['created_at'] = self.created_at.isoformat()
        new['updated_at'] = self.updated_at.isoformat()
        return new

    def __str__(self):
        """Return string representation of the class."""
        string = "["+str(self.__class__.__name__) +"] "
        string += "("+str(self.id)+") " + str(self.__dict__)
        return string
