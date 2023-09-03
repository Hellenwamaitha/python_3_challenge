# models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Establish relationship with reviews
    reviews = relationship("Review", back_populates="restaurant")

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Establish relationship with reviews
    reviews = relationship("Review", back_populates="customer")

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)

    # Define foreign keys
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Establish relationship with restaurant and customer
    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")
