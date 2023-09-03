"""Create Review table

Revision ID: f19d75952997
Revises: ca64d299c1e9
Create Date: 2023-09-03 20:04:45.994015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f19d75952997'
down_revision: Union[str, None] = 'ca64d299c1e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('star_rating', sa.Integer),
        sa.Column('restaurant_id', sa.Integer, sa.ForeignKey('restaurants.id')),
        sa.Column('customer_id', sa.Integer, sa.ForeignKey('customers.id')),
        # ... other columns if needed ...
    )

    # Create the foreign key relationships
    op.create_foreign_key('fk_reviews_restaurant', 'reviews', 'restaurants', ['restaurant_id'], ['id'])
    op.create_foreign_key('fk_reviews_customer', 'reviews', 'customers', ['customer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    # Drop the 'reviews' table
    op.drop_table('reviews')

    # Remove the foreign key relationships
    op.drop_constraint('fk_reviews_restaurant', 'reviews', type_='foreignkey')
    op.drop_constraint('fk_reviews_customer', 'reviews', type_='foreignkey')

    # ### end Alembic commands ###
