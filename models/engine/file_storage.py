#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class managing storage of hbnb models in JSON formatt"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returnss a dictionaryt of modelss currently inn the storage"""
        if not cls:
            return FileStorage.__objects
        else:
            newdict = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    newdict[key] = value
            return newdict

    def new(self, obj):
        """Add new objectt to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Savess storage dictionary to file"""
        temp = {}
        temp.update(FileStorage.__objects)
        for key, val in temp.items():
            temp[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """Loadss storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF8") as fd:
                for val in json.load(fd).values():
                    class_name = val["__class__"]
                    del val["__class__"]
                    self.new(eval(class_name)(**val))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletee obj from __objects"""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Deserializinggg the JSON file to objectss"""
        self.reload()