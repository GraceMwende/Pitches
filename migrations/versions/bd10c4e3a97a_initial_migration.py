"""Initial Migration

Revision ID: bd10c4e3a97a
Revises: d2fd32348bce
Create Date: 2022-02-10 12:55:15.466905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd10c4e3a97a'
down_revision = 'd2fd32348bce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_title', sa.String(), nullable=True))
    op.drop_constraint('comments_pitch_id_fkey', 'comments', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('comments_pitch_id_fkey', 'comments', 'pitches', ['pitch_id'], ['id'])
    op.drop_column('comments', 'pitch_title')
    # ### end Alembic commands ###
