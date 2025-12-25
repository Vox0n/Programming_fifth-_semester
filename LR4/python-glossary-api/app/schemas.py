from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TermBase(BaseModel):
    term: str
    definition: str
    category: Optional[str] = "General"
    example: Optional[str] = None


class TermCreate(TermBase):
    pass


class TermUpdate(BaseModel):
    definition: Optional[str] = None
    category: Optional[str] = None
    example: Optional[str] = None


class TermResponse(TermBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
