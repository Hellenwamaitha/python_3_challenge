from models import Customer, Restaurant, Review, sessionmaker
from sqlalchemy import create_engine
import random

# Create a session factory
Session = sessionmaker(bind=create_engine('sqlite:///mydatabase.db'))

# Predefined list of customer names and restaurant names
customer_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack']
restaurant_names = ['Restaurant A', 'Restaurant B', 'Restaurant C', 'Restaurant D', 'Restaurant E']

def create_fake_data():
    # Create a session
    session = Session()

    # Create customers from the predefined list
    customers = [Customer(name=name) for name in customer_names]

    # Create restaurants from the predefined list
    restaurants = [Restaurant(name=name, price=random.randint(1, 5)) for name in restaurant_names]

    # Create random reviews
    reviews = []
    for _ in range(20):
        random_customer = random.choice(customers)
        random_restaurant = random.choice(restaurants)
        star_rating = random.randint(1, 5)
        review = Review(star_rating=star_rating, customer=random_customer, restaurant=random_restaurant)
        reviews.append(review)

    # Add the instances to the session and commit to save them to the database
    session.add_all(customers + restaurants + reviews)
    session.commit()

    # Close the session when you're done
    session.close()

if __name__ == "__main__":
    # Generate and add data
    create_fake_data()
