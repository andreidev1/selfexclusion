"""empty message

Revision ID: 0d8c8e00f2cb
Revises: 
Create Date: 2022-12-03 20:56:24.822904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d8c8e00f2cb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('casino',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=240), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('cnp', sa.String(length=50), nullable=True),
    sa.Column('number_phone', sa.String(length=12), nullable=True),
    sa.Column('email_address', sa.String(length=60), nullable=True),
    sa.Column('selfie_kyc', sa.String(length=80), nullable=True),
    sa.Column('verified', sa.Boolean(), nullable=True),
    sa.Column('selected_casinos', sa.String(length=200), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['casino.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('casino')
    # ### end Alembic commands ###