#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DATETIME
from models import storageType


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models
    Attributes:
        id (sqlalchemy String): The BaseModel id.
        created_at (sqlalchemy DateTime): The datetime at creation.
        updated_at (sqlalchemy DateTime): The datetime of last update.
    """
    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DATETIME, nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for arg in kwargs:
                if arg in ['created_at', 'updated_at']:
                    setattr(self, arg, datetime.fromisoformat(kwargs[arg]))
                elif arg != '__class__':
                    setattr(self, arg, kwargs[arg])
            if storageType == 'db':
                if not hasattr(kwargs, 'id'):
                    setattr(self, 'id', str(uuid.uuid4()))
                if not hasattr(kwargs, 'created_at'):
                    setattr(self, 'created_at', datetime.now())
                if not hasattr(kwargs, 'updated_at'):
                    setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        print('In the to_dict duncttion')
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        for key in dictionary:
            if type(dictionary[key]) is datetime:
                dictionary[key] = dictionary[key].isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del(dictionary['_sa_instance_state'])
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        key = "{}.{}".format(type(self).__name__, self.id)
        del models.storage.__objects[key]
