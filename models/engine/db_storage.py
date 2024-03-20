#!/usr/bin/python3
"""This module contains the database storage engine"""

from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
from models.base_model import Base
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


if environ.get('HBNB_TYPE_STORAGE') == 'db':
    from models.place import place_amenity

HBNB_MYSQL_USER = environ.get('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = environ.get('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = environ.get('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = environ.get('HBNB_MYSQL_DB')

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
        env = environ.get("HBNB_ENV")

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
                self.__session.add(obj)

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
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """closes the working SQLAlchemy session"""
        self.__session.close()
