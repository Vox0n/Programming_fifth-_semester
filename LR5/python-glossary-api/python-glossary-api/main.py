from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import List

import crud, models, schemas
from database import SessionLocal, engine, get_db
from create_tables import create_tables  # Импортируем обновленную функцию

# Создаем таблицы и заполняем данными
create_tables()

# Создаем приложение FastAPI
app = FastAPI(
    title="Python Glossary API",
    description="API для глоссария терминов Python (с начальными данными)",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

@app.get("/terms", response_model=List[schemas.GlossaryTerm])
def read_terms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Получить все термины - теперь вернет 28 терминов"""
    terms = crud.get_terms(db, skip=skip, limit=limit)
    return terms

@app.get("/terms/category/{category}", response_model=List[schemas.GlossaryTerm])
def read_terms_by_category(category: str, db: Session = Depends(get_db)):
    """Получить термины по категории"""
    terms = db.query(models.GlossaryTerm)\
              .filter(models.GlossaryTerm.category == category)\
              .order_by(models.GlossaryTerm.term)\
              .all()
    return terms

# Остальные endpoint'ы остаются без изменений