from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db
from sqlalchemy import delete


def get_all(db: Session = Depends(get_db)):
    cars = db.query(models.Car).all()
    for car in cars:
        _ = car.model
        _ = car.brand
        _ = car.mileage
    return cars


def create_car(request: schemas.CarCreate, db: Session = Depends(get_db)):

    new_car = models.Car(
        model_id=request.model_id,
        brand_id=request.brand_id,
        user_id=request.user_id
    )

    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    _ = new_car.model
    _ = new_car.brand
    _ = new_car.mileage
    return new_car


def delete_car(car_id: int, db: Session = Depends(get_db)):
    car = db.get(models.Car, car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    db.delete(car)
    db.commit()
    return car


def update_car(request: schemas.CarUpdate, db: Session = Depends(get_db)):
    car = db.get(models.Car, request.id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    car_data = request.dict()
    for key, value in car_data.items():
        setattr(car, key, value)
    db.add(car)
    db.commit()
    db.refresh(car)
    _ = car.model
    _ = car.brand
    _ = car.mileage
    return car
