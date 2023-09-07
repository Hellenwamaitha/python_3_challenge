from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Define the one-to-many relationship between Restaurant and Review
    reviews = relationship('Review', back_populates='restaurant')

    # Define the many-to-many relationship between Restaurant and Customer through Review
    customers = relationship('Customer', secondary='reviews', overlaps="reviews")

    def all_reviews(self):
        return [review.full_review() for review in self.reviews]

    def average_rating(self):
        if not self.reviews:
            return None
        total_rating = sum(review.star_rating for review in self.reviews)
        return total_rating / len(self.reviews)

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Define the one-to-many relationship between Customer and Review
    reviews = relationship('Review', back_populates='customer')

    # Define the many-to-many relationship between Customer and Restaurant through Review
    restaurants = relationship('Restaurant', secondary='reviews', overlaps="reviews")

    def favorite_restaurant(self):
        if not self.reviews:
            return None
        favorite_review = max(self.reviews, key=lambda review: review.star_rating)
        return favorite_review.restaurant

    def restaurants(self):
        return [review.restaurant for review in self.reviews]

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)

    # Define foreign keys
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Define the many-to-one relationship between Review and Customer
    customer = relationship('Customer', back_populates='reviews', overlaps="restaurants")

    # Define the many-to-one relationship between Review and Restaurant
    restaurant = relationship('Restaurant', back_populates='reviews', overlaps="customers")

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.name}: {self.star_rating} stars"
