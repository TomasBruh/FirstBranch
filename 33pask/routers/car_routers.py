from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db
from repository import car_repository as rep

router = APIRouter(
    prefix='/api/cars',
    tags=['Cars']
)


@router.get('')
def get_all(db: Session = Depends(get_db)):
    return rep.get_all(db)


@router.post('/create')
def create_car(request: schemas.CarCreate, db: Session = Depends(get_db)):
    return rep.create_car(request, db)


@router.delete('/delete/{car_id}')
def delete_car(car_id: int, db: Session = Depends(get_db)):
    return rep.delete_car(car_id, db)


@router.patch('/update')
def update_car(request: schemas.CarUpdate, db: Session = Depends(get_db)):
    return rep.update_car(request, db)
