#!/usr/bin/python3
"""This is the base class"""


from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Base"""
    def __init__(self, *myargs, **mykwargs):
        """ init """
        ISO = '%Y-%m-%dT%H:%M:%S.%f'
        if mykwargs is not None and mykwargs != {}:
            for key, value in mykwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, ISO)

                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """ save method """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''to dict method'''
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy
  ''' 
    def to_dict(self):
        """To dict method"""
        iso_format_keys = {"created_at", "updated_at"}
        cy = {key: value.isoformat() if key in iso_format_keys and hasattr(value, 'isoformat') else value
                     for key, value in self.__dict__.items()}
        cy['__class__'] = self.__class__.__name__
        return cy    '''
        
        
    def __str__(self):
        """ __str__ method """
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

