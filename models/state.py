#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import storageType
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    print(f'In states page. storagetype: {storageType}')
    if storageType == 'db':
        print('In state if')
        name = Column(String(128), nullable=False)
        print('After name')
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
        print('after cities')
    else:
        name = ''

        @property
        def cities(self):
            '''returns the list of City instances with state_id
                equals the current State.id
                FileStorage relationship between State and City
            '''
            from models import storage
            res = []
            cities = storage.all(City)
            print('After cities in state')
            for city in cities.values():
                if city.state_id == self.id:
                    res.append(city)
            return res
