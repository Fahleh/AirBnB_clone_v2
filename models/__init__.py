#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import environ

storageType = environ.get('HBNB_TYPE_STORAGE')
print("Storage type set to:", storageType)

if storageType == 'db':
    print("Storage type in IF:", storageType)
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

storage.reload()
