"""empty message

Revision ID: 8d33bc8fb537
Revises: 5a69336d6bfd
Create Date: 2022-09-29 10:57:11.005342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d33bc8fb537'
down_revision = '5a69336d6bfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alumni', sa.Column('telephone', sa.String(length=10), nullable=True))
    op.add_column('person', sa.Column('gender', sa.String(), nullable=True))
    op.add_column('person', sa.Column('department', sa.String(), nullable=True))
    op.add_column('person', sa.Column('program', sa.String(), nullable=True))
    op.add_column('person', sa.Column('admitted', sa.Integer(), nullable=True))
    op.add_column('person', sa.Column('address', sa.String(), nullable=True))
    op.add_column('person', sa.Column('work', sa.String(), nullable=True))
    op.add_column('person', sa.Column('guardian', sa.String(), nullable=True))
    op.add_column('person', sa.Column('kin', sa.String(), nullable=True))
    op.add_column('person', sa.Column('relationship', sa.String(), nullable=True))
    op.add_column('person', sa.Column('marital', sa.String(), nullable=True))
    op.add_column('person', sa.Column('health', sa.String(), nullable=True))
    op.add_column('person', sa.Column('extra', sa.String(), nullable=True))
    op.add_column('person', sa.Column('image_file', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'image_file')
    op.drop_column('person', 'extra')
    op.drop_column('person', 'health')
    op.drop_column('person', 'marital')
    op.drop_column('person', 'relationship')
    op.drop_column('person', 'kin')
    op.drop_column('person', 'guardian')
    op.drop_column('person', 'work')
    op.drop_column('person', 'address')
    op.drop_column('person', 'admitted')
    op.drop_column('person', 'program')
    op.drop_column('person', 'department')
    op.drop_column('person', 'gender')
    op.drop_column('alumni', 'telephone')
    # ### end Alembic commands ###
