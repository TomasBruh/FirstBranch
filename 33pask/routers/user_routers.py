from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db
from repository import user_repository as rep

router = APIRouter(
    prefix='/api/users',
    tags=['Users']
)


@router.get('/get_all')
def get_all_users_and_settings(db: Session = Depends(get_db)):
    return rep.get_all_users_and_settings(db)


@router.delete("/delete/{user_id}")
def delete_user_and_his_settings(user_id: int, db: Session = Depends(get_db)):
    return rep.delete_user_and_his_settings(user_id, db)


@router.post('/create')
def create_user_with_settings(request: schemas.UserAndSettingsCreate, db: Session = Depends(get_db)):
    return rep.create_user_with_settings(request, db)


@router.patch("/update")
def update_user_and_his_settings(user_request: schemas.UserAndSettingsUpdate, db: Session = Depends(get_db)):
    return rep.update_user_and_his_settings(user_request, db)

