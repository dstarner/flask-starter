from sqlalchemy import Column, Integer, Text, Boolean, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()  # This is what all models must inherit from


class User(Base):  # Create our User class
    __tablename__ = 'users'  # What the database table will be called

    id = Column(Integer, primary_key=True)  # Every table needs a primary key to uniquely identity objects

    name = Column(String, nullable=False)   # The name inputted from the form

    frequency = Column(Integer, default=1)  # Start the name frequency at 1
