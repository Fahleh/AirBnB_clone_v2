#!/usr/bin/python3
"""This module contains the database storage engine"""

import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from os import getenv
from models.base_model import Base
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import placeAmenities

HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')

classes = {"User": User, "State": State, "City": City,
           "Amenity": Amenity, "Place": Place, "Review": Review}


class DBStorage:
    """database storage engine for mysql storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialise the new dbstorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB), pool_pre_ping=True)
        env = getenv("HBNB_ENV")

        if (env == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            query the current db session and list all instances of cls
        """
        dictionary = {}
        if cls is None:
            for item in classes.values():
                result = self.__session.query(item).all()
                for res in result:
                    key = res.__class__.__name__ + '.' + res.id
                    dictionary[key] = res
        else:
            result = self.__session.query(cls).all()
            for res in result:
                key = res.__class__.__name__ + '.' + res.id
                dictionary[key] = res
        return dictionary

    def new(self, obj):
        """
            Adds an object to the current db session
        """
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as execpt:
                self.__session.rollback()
                raise execpt

    def save(self):
        """Commit all changes made in the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """
            Deletes the object from the current databse session.
        """
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """Reloads the session"""
        print('IN RELOAD FUNCTION')
        Base.metadata.create_all(self.__engine)
        print('AFTER BASE.METADATA')
        session_factory = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
        print('AFER SESSION_FACTORY')
        self.__session = scoped_session(session_factory)()
        print('AFTER SESSION IS SET')

    def close(self):
        """closes the working SQLAlchemy session"""
        self.__session.close()
