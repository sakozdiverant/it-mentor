from alembic import op

# Revision identifiers, used by Alembic.
revision = 'your_revision_id'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None

def upgrade():
    # Удаление внешнего ключа
    op.drop_constraint('Заказы_КодКлиента_fkey', 'Заказы', type_='foreignkey')

def downgrade():
    # Восстановление внешнего ключа при откате миграции
    op.create_foreign_key(
        'Заказы_КодКлиента_fkey', 'Заказы', 'Клиенты',
        ['КодКлиента'], ['Код'], ondelete='CASCADE'  # Параметры по необходимости
    )
