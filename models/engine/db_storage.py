#!/usr/bin/python3
"""Contains db_storage"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from os import environ
from models.base_model import Base
from sqlalchemy.orm import scoped_session



class DBStorage():
    """DBStorage class"""
    class_list = ['State']
    #'Amenity', 'User', 'State', 'City', 'Review', 'Place'

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(environ.get('HBNB_MYSQL_USER'),
                                              environ.get('HBNB_MYSQL_PWD'),
                                              environ.get('HBNB_MYSQL_HOST'),
                                              environ.get('HBNB_MYSQL_DB')),
                                       pool_pre_ping=True)

        if environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """All method queries databasse for all objects"""
        dict = {}
        if cls is not None:
            objects = self.__session.query(cls.__name__)
            for obj in objects:
                str = cls.__name__ + '.' + obj.id
                dict[str] = obj
        else:
            try:
                for clss in self.class_list:
                    objects = self.__session.query(clss)
                    for obj in objects:
                        str = cls.__name__ + '.' + obj.id
                        dict[str] = obj
            except:
                pass
        return dict

    def new(self, obj):
        """Adds object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Saves current database session"""
        self.__session.commit()

    def delete(self, obj):
        """Deletes and object from current database session"""
        self.__session.delete(obj)

    def reload(self):
        """Creates all tables in database"""
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.user import User
        from models.review import Review
        from models.place import Place
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
