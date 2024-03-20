#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storageType
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Defines an amenity Class"""
    __tablename__ = 'amenities'
    if storageType == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
