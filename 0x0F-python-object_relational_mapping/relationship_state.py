#!/usr/bin/python3
"""
<<<<<<< HEAD
This script defines a State class
=======
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
>>>>>>> 69af24936ba87cf68953d27ac5b93a68baf2b29c
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
<<<<<<< HEAD
=======

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
        cities (:obj:`City`): The Cities belongs to State

>>>>>>> 69af24936ba87cf68953d27ac5b93a68baf2b29c
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
