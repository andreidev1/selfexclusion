"""empty message

Revision ID: e91c2132d789
Revises: 
Create Date: 2022-12-25 01:20:49.394446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e91c2132d789'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=24), nullable=True),
    sa.Column('password', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('casino',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=240), nullable=True),
    sa.Column('email', sa.String(length=240), nullable=True),
    sa.Column('timestamp', sa.String(length=500), nullable=True),
    sa.Column('auth_key', sa.String(length=500), nullable=True),
    sa.Column('verified', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('cnp', sa.String(length=50), nullable=True),
    sa.Column('number_phone', sa.String(length=12), nullable=True),
    sa.Column('email_address', sa.String(length=60), nullable=True),
    sa.Column('selfie_kyc', sa.String(length=80), nullable=True),
    sa.Column('selected_casinos', sa.String(length=200), nullable=True),
    sa.Column('period', sa.String(length=200), nullable=True),
    sa.Column('timestamp', sa.String(length=500), nullable=True),
    sa.Column('verified', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('casino')
    op.drop_table('admin')
    # ### end Alembic commands ###
