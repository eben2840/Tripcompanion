"""empty message

Revision ID: b6bff13c5f3a
Revises: 879ec797f9ca
Create Date: 2023-06-07 15:47:27.794479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6bff13c5f3a'
down_revision = '879ec797f9ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chatus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chatme', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chatus')
    # ### end Alembic commands ###
