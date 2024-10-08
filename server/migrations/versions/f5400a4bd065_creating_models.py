"""Creating Models

Revision ID: f5400a4bd065
Revises: 
Create Date: 2024-10-06 16:55:05.887496

"""
from alembic import op
import sqlalchemy as sa


revision = 'f5400a4bd065'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('heroes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('super_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('powers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hero_powers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strength', sa.String(), nullable=False),
    sa.Column('hero_id', sa.Integer(), nullable=True),
    sa.Column('power_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hero_id'], ['heroes.id'], name=op.f('fk_hero_powers_hero_id_heroes'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['power_id'], ['powers.id'], name=op.f('fk_hero_powers_power_id_powers'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('hero_powers')
    op.drop_table('powers')
    op.drop_table('heroes')
