"""empty message

Revision ID: 3872d2c85f25
Revises: b510973ced08
Create Date: 2018-06-30 09:17:57.125986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3872d2c85f25"
down_revision = "b510973ced08"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "comment",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("post_id", sa.Integer(), nullable=True),
        sa.Column("parent_id", sa.Integer(), nullable=True),
        sa.Column("messages", sa.Text(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("is_spam", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(["parent_id"], ["comment.id"]),
        sa.ForeignKeyConstraint(["post_id"], ["post.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["user.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_comment_parent_id"), "comment", ["parent_id"], unique=False
    )
    op.add_column("feed", sa.Column("user_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "feed", "user", ["user_id"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "feed", type_="foreignkey")
    op.drop_column("feed", "user_id")
    op.drop_index(op.f("ix_comment_parent_id"), table_name="comment")
    op.drop_table("comment")
    # ### end Alembic commands ###
