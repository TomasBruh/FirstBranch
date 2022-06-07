from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/cars',
    tags=['Cars']
)


@router.get('', response_model=List[schemas.CarAll])
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Car).all()


@router.post('/create')
def create_car(request: schemas.CarCreate, db: Session = Depends(get_db)):

    new_car = models.Car(
        mileage=request.mileage,
        brand_model_id=request.brand_mileage_id
    )

    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return new_car
