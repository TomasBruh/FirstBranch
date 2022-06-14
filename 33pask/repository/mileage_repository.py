from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db
from sqlalchemy import delete


def get_all_mileages(db: Session = Depends(get_db)):
    return db.query(models.CarMileage).all()


def create_mileage(request: schemas.CarMileageCreate, db: Session = Depends(get_db)):
    new_mileage = models.CarMileage(
        distance=request.distance,
        car_id=request.car_id
    )

    db.add(new_mileage)
    db.commit()
    db.refresh(new_mileage)

    return new_mileage


def delete_mileage(mileage_id: int, db: Session = Depends(get_db)):
    mileage = db.get(models.CarMileage, mileage_id)
    if mileage is None:
        raise HTTPException(status_code=404, detail="Mileage not found")
    db.delete(mileage)
    db.commit()
    return mileage


def update_mileage(request: schemas.CarMileageUpdate, db: Session = Depends(get_db)):
    mileage_record = db.get(models.CarMileage, request.id)
    if mileage_record is None:
        raise HTTPException(status_code=404, detail="Mileage not found")
    mileage_record_data = request.dict()
    for key, value in mileage_record_data.items():
        setattr(mileage_record, key, value)

    db.add(mileage_record)
    db.commit()
    db.refresh(mileage_record)
    return mileage_record

