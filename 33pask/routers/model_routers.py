from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db
from repository import model_repository as rep


router = APIRouter(
    prefix='/api/model',
    tags=['Models']
)


@router.get('/get_all')
def get_all(db: Session = Depends(get_db)):
    return rep.get_all(db)


@router.post('/create')
def create_model(request: schemas.CarModelCreate, db: Session = Depends(get_db)):
    return rep.create_model(request, db)


@router.delete('/delete/{model_id}')
def delete_model(model_id: int, db: Session = Depends(get_db)):
    return rep.delete_model(model_id, db)


@router.patch('/update')
def update_model(request: schemas.CarModelUpdate, db: Session = Depends(get_db)):
    return rep.update_model(request, db)
