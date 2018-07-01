"""empty message

Revision ID: a4702859796a
Revises: fbfec56d097e
Create Date: 2018-06-27 10:11:35.674759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a4702859796a"
down_revision = "fbfec56d097e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("post", sa.Column("owner", sa.String(length=150), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("post", "owner")
    # ### end Alembic commands ###
