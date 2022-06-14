from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db
from sqlalchemy import delete


def get_all(db: Session = Depends(get_db)):
    brands = db.query(models.CarBrand).all()
    for brand in brands:
        _ = brand.models
        _ = brand.cars
    return brands


def create_brand(request: schemas.CarBrandCreate, db: Session = Depends(get_db)):
    new_brand = models.CarBrand(
        name=request.name,
        founded_in_year=request.founded_in_year
    )
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)
    _ = new_brand.models
    _ = new_brand.cars
    return new_brand


def update_car_brand(request: schemas.CarBrandUpdate, db: Session = Depends(get_db)):
    car_brand = db.get(models.CarBrand, request.id)
    if car_brand is None:
        raise HTTPException(status_code=404, detail="Car brand was not found")
    car_brand_data = request.dict()
    for key, value in car_brand_data.items():
        if key != 'settings':
            setattr(car_brand, key, value)
    _ = car_brand.models
    _ = car_brand.cars
    db.add(car_brand)
    db.commit()
    db.refresh(car_brand)
    return car_brand


def delete_car_brand(brand_id: int, db: Session = Depends(get_db)):
    car_brand = db.get(models.CarBrand, brand_id)
    if car_brand is None:
        raise HTTPException(status_code=404, detail="Car brand was not found")
    _ = car_brand.models
    _ = car_brand.cars
    db.delete(car_brand)
    db.commit()
    return car_brand

