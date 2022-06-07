from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/brand',
    tags=['Brands']
)


@router.get('', response_model=List[schemas.CarBrandAll])
def get_all(db: Session = Depends(get_db)):
    return db.query(models.CarBrand).all()


@router.post('/create')
def create_brand(request: schemas.CarBrandCreate, db: Session = Depends(get_db)):

    new_brand = models.CarBrand(
        name=request.name,
        founded_in_year=request.founded_in_year
    )

    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)

    return new_brand
