from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from repository import brand_repository as rep

router = APIRouter(
    prefix='/api/brand',
    tags=['Brands']
)


@router.get('')
def get_all(db: Session = Depends(get_db)):
    return rep.get_all(db)


@router.post('/create')
def create_brand(request: schemas.CarBrandCreate, db: Session = Depends(get_db)):
    return rep.create_brand(request, db)


@router.patch("/update") # {brand_id}??????????????????????
def update_car_brand(request: schemas.CarBrandUpdate, db: Session = Depends(get_db)):
    return rep.update_car_brand(request, db)


@router.delete("/delete/{brand_id}")
def delete_car_brand(brand_id: int, db: Session = Depends(get_db)):
    return rep.delete_car_brand(brand_id, db)

