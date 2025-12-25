from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
import models
import schemas
from database import engine, SessionLocal
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Python Glossary API", version="1.0.0")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {
        "message": "Python Glossary API",
        "endpoints": {
            "GET /terms": "Get all terms",
            "GET /terms/{id}": "Get term by ID",
            "POST /terms": "Create new term",
            "PUT /terms/{id}": "Update term",
            "DELETE /terms/{id}": "Delete term",
            "GET /search": "Search terms",
            "GET /categories": "Get all categories"
        }
    }


@app.get("/terms", response_model=List[schemas.TermResponse])
def get_terms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Получить все термины с пагинацией"""
    terms = db.query(models.Term).offset(skip).limit(limit).all()
    return terms


@app.get("/terms/{term_id}", response_model=schemas.TermResponse)
def get_term(term_id: int, db: Session = Depends(get_db)):
    """Получить термины по ID"""
    term = db.query(models.Term).filter(models.Term.id == term_id).first()
    if not term:
        raise HTTPException(status_code=404, detail="Term not found")
    return term


@app.post("/terms", response_model=schemas.TermResponse)
def create_term(term: schemas.TermCreate, db: Session = Depends(get_db)):
    """Создать новый термины"""

    existing = db.query(models.Term).filter(models.Term.term == term.term).first()
    if existing:
        raise HTTPException(status_code=400, detail="Term already exists")

    db_term = models.Term(**term.dict())
    db.add(db_term)
    db.commit()
    db.refresh(db_term)
    return db_term


@app.put("/terms/{term_id}", response_model=schemas.TermResponse)
def update_term(term_id: int, term_data: schemas.TermUpdate, db: Session = Depends(get_db)):
    """Обновить термины"""
    term = db.query(models.Term).filter(models.Term.id == term_id).first()
    if not term:
        raise HTTPException(status_code=404, detail="Term not found")

    for key, value in term_data.dict(exclude_unset=True).items():
        setattr(term, key, value)

    db.commit()
    db.refresh(term)
    return term


@app.delete("/terms/{term_id}")
def delete_term(term_id: int, db: Session = Depends(get_db)):
    """Удалить термины"""
    term = db.query(models.Term).filter(models.Term.id == term_id).first()
    if not term:
        raise HTTPException(status_code=404, detail="Term not found")

    db.delete(term)
    db.commit()
    return {"message": "Term deleted successfully"}


@app.get("/search")
def search_terms(q: str, db: Session = Depends(get_db)):
    """Поиск терминов по названию или определению"""
    terms = db.query(models.Term).filter(
        models.Term.term.ilike(f"%{q}%") |
        models.Term.definition.ilike(f"%{q}%")
    ).all()
    return terms


@app.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    """Получить все категории"""
    categories = db.query(models.Term.category).distinct().all()
    return [cat[0] for cat in categories]


@app.get("/categories/{category}")
def get_terms_by_category(category: str, db: Session = Depends(get_db)):
    """Получить термины по категории"""
    terms = db.query(models.Term).filter(models.Term.category == category).all()
    return terms
