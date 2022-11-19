"""empty message

Revision ID: c04481b855bd
Revises: 7c642e54d680
Create Date: 2022-11-19 08:28:47.687951

"""
from alembic import op
import sqlalchemy as sa
from migrations.models.currency import Currency


# revision identifiers, used by Alembic.
revision = 'c04481b855bd'
down_revision = '7c642e54d680'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(op.f('uq__currency__id'), 'currency', ['id'])
    op.create_unique_constraint(op.f('uq__currency_account__id'), 'currency_account', ['id'])
    op.create_unique_constraint(op.f('uq__news__id'), 'news', ['id'])
    op.create_unique_constraint(op.f('uq__transactions__id'), 'transactions', ['id'])
    op.add_column('users', sa.Column('phone', sa.String(), nullable=False))
    op.drop_constraint('uq__users__email', 'users', type_='unique')
    op.drop_constraint('uq__users__username', 'users', type_='unique')
    op.create_unique_constraint(op.f('uq__users__phone'), 'users', ['phone'])
    op.drop_column('users', 'email')
    op.drop_column('users', 'username')
    bind = op.get_bind() 
    session = sa.orm.Session(bind=bind)
    query1 = sa.insert(Currency).values(
        name="rub",
        fullname="Rubles",
        value=1.0
    )
    query2 = sa.insert(Currency).values(
        name="usd",
        fullname="American dollars",
        value=60.0
    )
    query3 = sa.insert(Currency).values(
        name="eur",
        fullname="Euro",
        value=60.0
    )
    session.execute(query1)
    session.execute(query2)
    session.execute(query3)
    session.commit()
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(op.f('uq__users__phone'), 'users', type_='unique')
    op.create_unique_constraint('uq__users__username', 'users', ['username'])
    op.create_unique_constraint('uq__users__email', 'users', ['email'])
    op.drop_column('users', 'phone')
    op.drop_constraint(op.f('uq__transactions__id'), 'transactions', type_='unique')
    op.drop_constraint(op.f('uq__news__id'), 'news', type_='unique')
    op.drop_constraint(op.f('uq__currency_account__id'), 'currency_account', type_='unique')
    op.drop_constraint(op.f('uq__currency__id'), 'currency', type_='unique')
    # ### end Alembic commands ###