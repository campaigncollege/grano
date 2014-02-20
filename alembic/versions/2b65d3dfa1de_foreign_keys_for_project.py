"""foreign keys for project

Revision ID: 2b65d3dfa1de
Revises: 40941ab93ba
Create Date: 2014-02-16 13:19:42.398726

"""

# revision identifiers, used by Alembic.
revision = '2b65d3dfa1de'
down_revision = '40941ab93ba'

import uuid
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


def upgrade():
    account = table('account',
        column('login', sa.String),
        column('api_key', sa.String)
    )
    engine = op.get_bind()

    op.execute(account.insert().values({'login': '_system', 'api_key': uuid.uuid4().hex}))

    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entity', sa.Column('author_id', sa.Integer(), nullable=True))
    op.add_column('entity', sa.Column('project_id', sa.Integer(), nullable=True))
    op.add_column('project', sa.Column('author_id', sa.Integer(), nullable=True))
    
    if engine.dialect.name != 'sqlite':
        op.drop_column('project', 'owner_id')
    
    op.add_column('property', sa.Column('author_id', sa.Integer(), nullable=True))
    op.add_column('relation', sa.Column('author_id', sa.Integer(), nullable=True))
    op.add_column('relation', sa.Column('project_id', sa.Integer(), nullable=True))
    op.add_column('schema', sa.Column('project_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('schema', 'project_id')
    op.drop_column('relation', 'project_id')
    op.drop_column('relation', 'author_id')
    op.drop_column('property', 'author_id')
    op.add_column('project', sa.Column('owner_id', sa.INTEGER(), nullable=True))
    op.drop_column('project', 'author_id')
    op.drop_column('entity', 'project_id')
    op.drop_column('entity', 'author_id')
    ### end Alembic commands ###
