#!/usr/bin/python3
"""module defineing class managing db storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """hte SQL database storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Creating engine and connecting to database"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV", "none")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        if envv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returning a dictionary
        Return:
            returning a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)

    def new(self, obj):
        """add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from current db session object if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create current db session from the engine
        using sessionmaker"""
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        """Removing session"""
        self.__session.close()