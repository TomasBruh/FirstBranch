from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import get_db
from sqlalchemy import delete


def get_all_users_and_settings(db: Session = Depends(get_db)):
    all_users = db.query(models.User).all()
    for user in all_users:
        _ = user.settings
        for car in user.cars:
            _ = car.brand
            _ = car.model
            _ = car.mileage
    return all_users


def delete_user_and_his_settings(user_id: int, db: Session = Depends(get_db)):
    user = db.get(models.User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    settings = user.settings
    db.delete(user)
    db.commit()
    db.delete(settings)
    db.commit()
    return user


def create_user_with_settings(request: schemas.UserAndSettingsCreate, db: Session = Depends(get_db)):
    new_user_settings = models.UserSettings(
        consumption_is_eu=request.settings.consumption_is_eu,
        odometer_is_eu=request.settings.odometer_is_eu
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
    _ = new_user.settings
    return new_user


def update_user_and_his_settings(user_request: schemas.UserAndSettingsUpdate, db: Session = Depends(get_db)):
    user = db.get(models.User, user_request.id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user_request.dict()
    user_settings = db.get(models.UserSettings, user.settings_id)
    if not user_settings:
        raise HTTPException(status_code=404, detail="User's settings not found")
    for key, value in user_data.items():
        if key != 'settings':
            setattr(user, key, value)
    user_settings.consumption_is_eu = user_request.settings.consumption_is_eu
    user_settings.odometer_is_eu = user_request.settings.odometer_is_eu
    db.add(user_settings)
    db.commit()
    db.refresh(user_settings)
    db.add(user)
    db.commit()
    db.refresh(user)
    _ = user.settings
    return user

