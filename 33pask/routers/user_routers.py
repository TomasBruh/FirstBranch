from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/users',
    tags=['Users']
)


@router.get('', response_model=List[schemas.UserAll])
def get_all(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.post('/create')
def create_user(request: schemas.UserCreate, request_settings: schemas.UserSettingsCreate, db: Session = Depends(get_db)):
    new_user_settings = models.UserSettings(
        consumption_is_eu=request_settings.consumption_is_eu,
        odometer_is_eu=request_settings.odometer_is_eu
    )

    db.add(new_user_settings)
    db.commit()
    db.refresh(new_user_settings)

    new_user = models.User(
        email=request.email,
        first_name=request.first_name,
        last_name=request.last_name,
        settings=new_user_settings
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
