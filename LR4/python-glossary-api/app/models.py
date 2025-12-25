from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Term(Base):
    # Имя таблицы в БД
    __tablename__ = "terms"

    # Поля таблицы
    id = Column(Integer, primary_key=True, index=True)
    term = Column(String, unique=True, index=True, nullable=False)  # Название термина (уникальное)
    definition = Column(Text, nullable=False)                        # Объяснение
    example = Column(Text, nullable=True)                            # Пример кода (необязательное)
