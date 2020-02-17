#!/usr/bin/python3
from datetime import datetime
import uuid
import json
import models
""" BaseModel python file """


class BaseModel:
    """ Class BaseModel """

    def __init__(self, *args, **kwargs):
        """ initialize variables, dict to class """
        if not (kwargs):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

        else:
            for key, value in kwargs.items():
                if key is '__class__' :
                    pass
                elif key is 'created_at' or key is 'updated_at':
                    value = datetime.strptime(value,'%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)

    def __str__(self):
        """ return string with info on class """
        name = self.__class__.__name__
        return ("[{}] ({}) {}".format(name, self.id, self.__dict__))

    def save(self):
        """ func to update time """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """ func to createa dictionary of of class elements """
        mydict = dict(self.__dict__)
        mydict.update({"__class__": "BaseModel"})
        created = mydict.get("created_at").strftime("%Y-%m-%dT%H:%M:%S.%f")
        mydict.update({"created_at": created})
        update = mydict.get("updated_at").strftime("%Y-%m-%dT%H:%M:%S.%f")
        mydict.update({"updated_at": update})
        return (mydict)
