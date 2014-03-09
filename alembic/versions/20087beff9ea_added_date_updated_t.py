"""Added date updated to Owner

Revision ID: 20087beff9ea
Revises: 2dc72d16c188
Create Date: 2014-03-09 01:43:00.648013

"""

# revision identifiers, used by Alembic.
revision = '20087beff9ea'
down_revision = '2dc72d16c188'

from alembic import op
import sqlalchemy as sa

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('owner', sa.Column('date_updated', sa.DateTime()))
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('owner', 'date_updated')
    ### end Alembic commands ###

