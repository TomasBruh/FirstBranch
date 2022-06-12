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


@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(models.User, user_id)
    # if not hero:
    #     raise HTTPException(status_code=404, detail="Hero not found")
    db.delete(user)
    db.commit()
    return user


@router.patch("/update")
def update_user(user_request: schemas.UserUpdate, settings_request: schemas.UserSettingsUpate,
                db: Session = Depends(get_db)):
    user = db.get(models.User, user_request.user_id)
    # if not db_hero:
    #     raise HTTPException(status_code=404, detail="Hero not found")
    user_settings = db.get(models.UserSettings, settings_request.settigs_id)
    user_settings_data = user_settings.dict(exclude_unset=True)
    user_data = user_request.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
