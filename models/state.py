#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.sql.expression import null
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
    #, cascade="all, delete-orphan", passive_deletes=True

    @property
    def cities(self):
        """Getter for cities"""
        return 
