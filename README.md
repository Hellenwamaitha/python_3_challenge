# python_3_challenge
# SQLAlchemy Migrations and Object Relationships Project

## Introduction
This project revolves around utilizing SQLAlchemy, a widely-used Object Relational Mapping (ORM) library for Python. Our objectives encompass database schema migrations, the establishment of object relationships, and the implementation of a range of methods to interact with our models. These models include classes such as Restaurant, Customer, and Review. The following README will provide a comprehensive guide for the tasks and expected deliverables.
Prerequisites
Before diving into the project, ensure you have the following in place:

### SQLAlchemy installed.
    Initial Restaurant and Customer models, database tables, and sample data.
    A reviews table created via migration, including columns to establish relationships with Restaurant and Customer, as well as a star_rating column to store review ratings.

## Migration

    Create a migration for the reviews table with the necessary columns to establish relationships with Restaurant and Customer. Include a star_rating column to store review ratings.

### Object Relationship Methods
#### Review Class

    customer(): Returns the Customer instance associated with this review.
    restaurant(): Returns the Restaurant instance associated with this review.

#### Restaurant Class

    reviews(): Returns a collection of all the reviews for the restaurant.
    customers(): Returns a collection of all the customers who reviewed the restaurant.

#### Customer Class

    reviews(): Returns a collection of all the reviews that the customer has left.
    restaurants(): Returns a collection of all the restaurants that the customer has reviewed.

## Aggregate and Relationship Methods
#### Customer Class

    full_name(): Returns the full name of the customer, with the first name and last name concatenated.
    favorite_restaurant(): Returns the restaurant instance with the highest star rating from this customer.
    add_review(restaurant, rating): Creates a new review for the specified restaurant with the given rating.
    delete_reviews(restaurant): Removes all reviews by the customer for a specific restaurant.

#### Review Class

    full_review(): Returns a formatted review string, e.g., "Review for {restaurant name} by {customer's full name}: {review star_rating} stars."

#### Restaurant Class

    fanciest(): Returns one restaurant instance with the highest price.
    all_reviews(): Returns a list of strings with all the reviews for this restaurant, formatted as specified.

## Usage

    Create database tables and initial data using migrations and the seeds.py file.
    Implement methods and test them in the console using sample data.
    Follow the suggested order of tasks, but feel free to adapt based on your preference.
    Ensure methods work as expected and test thoroughly before proceeding.
    Refactor code for clean and maintainable organization.

This project does  include automated tests. 

## License

This project is open-source and available under the MIT License.

## MIT License

Copyright (c) 2023 Hellen Wamaitha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.