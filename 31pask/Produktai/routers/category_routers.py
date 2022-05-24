from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/categories',
    tags=['Categories']
)


@router.get('', response_model=List[schemas.CategoryAll])
def all(db: Session = Depends(get_db)):
    return db.query(models.Category).all()


@router.post('/create')
def create_category(request: schemas.CategoryCreate, db: Session = Depends(get_db)):
    new_category = models.Category(
        name=request.name,
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category