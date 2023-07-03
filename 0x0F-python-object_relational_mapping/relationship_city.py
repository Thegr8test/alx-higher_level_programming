#!/usr/bin/python3
"""
This script defines a City class
<<<<<<< HEAD
=======
to work with MySQLAlchemy ORM.
>>>>>>> 69af24936ba87cf68953d27ac5b93a68baf2b29c
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
<<<<<<< HEAD
=======

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The id of the class
        name (str): The name of the class
        state_id (int): The state the city belongs to

>>>>>>> 69af24936ba87cf68953d27ac5b93a68baf2b29c
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
