"""empty message

Revision ID: 6ab1e0a57398
Revises: 3b8fb366953e
Create Date: 2021-01-19 22:24:52.606509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ab1e0a57398'
down_revision = '3b8fb366953e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tiny_text', sa.Column('pw_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_tiny_text_votes'), 'tiny_text', ['votes'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tiny_text_votes'), table_name='tiny_text')
    op.drop_column('tiny_text', 'pw_hash')
    # ### end Alembic commands ###
