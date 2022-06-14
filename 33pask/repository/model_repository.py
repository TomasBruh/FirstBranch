from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db
from sqlalchemy import delete


def get_all(db: Session = Depends(get_db)):
    car_models = db.query(models.CarModel).all()
    for car_model in car_models:
        _ = car_model.cars
    return car_models


def create_model(request: schemas.CarModelCreate, db: Session = Depends(get_db)):
    new_model = models.CarModel(
        name=request.name,
        brand_id=request.brand_id
    )
    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    _ = new_model.cars
    return new_model


def delete_model(model_id: int, db: Session = Depends(get_db)):
    car_model = db.get(models.CarModel, model_id)
    if car_model is None:
        raise HTTPException(status_code=404, detail="Car model was not found")
    _ = car_model.cars
    db.delete(car_model)
    db.commit()
    return car_model


def update_model(request: schemas.CarModelUpdate, db: Session = Depends(get_db)):
    car_model = db.get(models.CarModel, request.id)
    if car_model is None:
        raise HTTPException(status_code=404, detail="Car model was not found")
    car_model_data = request.dict()
    for key, value in car_model_data.items():
        if key != 'settings':
            setattr(car_model, key, value)

    db.add(car_model)
    db.commit()
    db.refresh(car_model)
    _ = car_model.cars
    return car_model
