from database import init_db


def create_tables():
    """Создает только таблицы через SQLAlchemy"""
    print("Creating database tables...")
    init_db()
    print("Database tables created")

    # Заполнение базы теперь отдельно
    # import seed_database
    # seed_database.seed_database()