from pydantic import BaseModel
from typing import Optional

# Схема для создания нового термина (то, что присылает пользователь)
class TermCreate(BaseModel):
    term: str
    definition: str
    example: Optional[str] = None

# Схема для обновления термина (все поля необязательные)
class TermUpdate(BaseModel):
    term: Optional[str] = None
    definition: Optional[str] = None
    example: Optional[str] = None

# Схема для ответа API (то, что мы отправляем пользователю)
class TermResponse(BaseModel):
    id: int
    term: str
    definition: str
    example: Optional[str] = None

    # Настройка для работы с SQLAlchemy (преобразует объект БД в dict)
    class Config:
        from_attributes = True
