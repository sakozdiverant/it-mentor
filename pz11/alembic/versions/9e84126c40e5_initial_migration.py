"""Initial migration

Revision ID: 9e84126c40e5
Revises: 
Create Date: 2024-09-07 13:45:39.597902

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e84126c40e5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('documents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_documents_id'), 'documents', ['id'], unique=False)
    op.create_table('documents_text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_doc', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_doc'], ['documents.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_documents_text_id'), 'documents_text', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_documents_text_id'), table_name='documents_text')
    op.drop_table('documents_text')
    op.drop_index(op.f('ix_documents_id'), table_name='documents')
    op.drop_table('documents')
    # ### end Alembic commands ###