from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db


router = APIRouter(
    prefix='/api/mileage',
    tags=['Mileage']
)


@router.post('/create')
def create_mileage(request: schemas.CarMileageCreate, db: Session = Depends(get_db)):
    new_mileage = models.CarMileage(
        distance=request.distance,
        car_id=request.car_id
    )

    db.add(new_mileage)
    db.commit()
    db.refresh(new_mileage)

    return new_mileage
