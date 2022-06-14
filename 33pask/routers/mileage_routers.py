from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from repository import mileage_repository as rep

router = APIRouter(
    prefix='/api/mileage',
    tags=['Mileage']
)


@router.get('')
def get_all_mileages(db: Session = Depends(get_db)):
    return rep.get_all_mileages(db)


@router.post('/create')
def create_mileage(request: schemas.CarMileageCreate, db: Session = Depends(get_db)):
    return rep.create_mileage(request, db)


@router.delete('/delete/{mileage_id}')
def delete_mileage(mileage_id: int, db: Session = Depends(get_db)):
    return rep.delete_mileage(mileage_id, db)


@router.patch('/update')
def update_mileage(request: schemas.CarMileageUpdate, db: Session = Depends(get_db)):
    return rep.update_mileage(request, db)

