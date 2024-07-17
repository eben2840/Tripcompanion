"""empty message

Revision ID: 55a14cec9183
Revises: 3fdb0c17b240
Create Date: 2024-07-17 17:26:23.067952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55a14cec9183'
down_revision = '3fdb0c17b240'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locationsearch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=True),
    sa.Column('center', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('link', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('about', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('desc', sa.String(), nullable=True))
        batch_op.alter_column('arrears',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('arrears',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=True)
        batch_op.drop_column('desc')
        batch_op.drop_column('about')
        batch_op.drop_column('link')

    op.drop_table('locationsearch')
    # ### end Alembic commands ###
