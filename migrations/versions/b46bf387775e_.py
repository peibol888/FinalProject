"""empty message
Revision ID: b46bf387775e
Revises: 6fb273ef557b
Create Date: 2021-12-07 19:42:09.710271
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b46bf387775e'
down_revision = '6fb273ef557b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('profile_image_url', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'profile_image_url')
    # ### end Alembic commands ###