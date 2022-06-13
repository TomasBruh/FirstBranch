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


@router.get('')
def get_all(db: Session = Depends(get_db)):
    cars = db.query(models.Car).all()
    for car in cars:
        _ = car.model
        _ = car.brand
        _ = car.mileage
    return cars


@router.post('/create')
def create_car(request: schemas.CarCreate, db: Session = Depends(get_db)):

    new_car = models.Car(
        model_id=request.model_id,
        brand_id=request.brand_id,
        user_id=request.user_id
    )

    db.add(new_car)
    db.commit()
    db.refresh(new_car)

    return new_car


@router.delete('/delete/{car_id}')
def delete_car(car_id: int, db: Session = Depends(get_db)):
    car = db.get(models.Car, car_id)
    db.delete(car)
    db.commit()
    return car


@router.patch('/update')
def update_car(request: schemas.CarUpdate, db: Session = Depends(get_db)):
    car = db.get(models.Car, request.id)
    car_data = request.dict()
    for key, value in car_data.items():
        setattr(car, key, value)
    _ = car.model
    _ = car.brand
    _ = car.mileage
    db.add(car)
    db.commit()
    db.refresh(car)
    return car
