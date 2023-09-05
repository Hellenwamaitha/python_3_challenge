# display_data.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate  # Assuming you have tabulate installed

from models import Customer, Restaurant, Review

def display_fake_data():
    # Create a session factory
    Session = sessionmaker(bind=create_engine('sqlite:///mydatabase.db'))

    # Create a session
    session = Session()

    # Query the database to retrieve fake data
    customers = session.query(Customer).all()
    restaurants = session.query(Restaurant).all()
    reviews = session.query(Review).all()

    # Prepare data for tabulation
    customer_data = [(customer.id, customer.name) for customer in customers]
    restaurant_data = [(restaurant.id, restaurant.name, restaurant.price) for restaurant in restaurants]
    review_data = [(review.id, review.star_rating, review.customer.name, review.restaurant.name) for review in reviews]

    # Display data in tabular format
    print("Customers:")
    print(tabulate(customer_data, headers=["ID", "Name"], tablefmt="grid"))
    print("\nRestaurants:")
    print(tabulate(restaurant_data, headers=["ID", "Name", "Price"], tablefmt="grid"))
    print("\nReviews:")
    print(tabulate(review_data, headers=["ID", "Rating", "Customer", "Restaurant"], tablefmt="grid"))

    # Close the session when done
    session.close()

if __name__ == "__main__":
    # Call the display_fake_data function to display the data
    display_fake_data()
