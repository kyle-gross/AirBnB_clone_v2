#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.sql.expression import null
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
    #, cascade="all, delete-orphan", passive_deletes=True

    @property
    def cities(self):
        """Getter for cities"""
        from models import storage
        lst = []
        for k, v in storage.all(City):
            if self.id == v.state_id:
                lst.append(v)
        return lst


