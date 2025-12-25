from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем файл базы данных "glossary.db" в текущей папке
SQLALCHEMY_DATABASE_URL = "sqlite:///./glossary.db"

# Создаем "движок" для подключения к БД
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Создаем фабрику для сессий работы с БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для создания моделей (таблиц) БД
Base = declarative_base()

# Функция для получения сессии БД (используется в эндпоинтах FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
