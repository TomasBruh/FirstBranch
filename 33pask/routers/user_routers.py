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


@router.get('')  # RESPONSE MODEL!!!!!!!!!!!!!!!!!!!!!!!
def get_all_users_and_settings(db: Session = Depends(get_db)):
    all_users = db.query(models.User).all()
    all_settings = db.query(models.UserSettings).all()

    for user in all_users:
        getattr()
        # settings_id = user.settings_id
        # setattr(user, "settings", all_settings)

    # test_list = []
    # for i in range(len(all_users)):
    #     thing = {
    #         "settings": all_settings[i],
    #         "IDK": all_users[i]
    #     }
    #     test_list.append(
    #         thing
    #     )
    return all_settings


@router.post('/create')
def create_user_with_settings(request: schemas.UserCreate, request_settings: schemas.UserSettingsCreate,
                              db: Session = Depends(get_db)):
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
def delete_user_and_his_settings(user_id: int, db: Session = Depends(get_db)):
    user = db.get(models.User, user_id)
    settings = db.get(models.UserSettings, user.settings_id)
    # if not hero:
    #     raise HTTPException(status_code=404, detail="Hero not found")
    db.delete(user)
    db.commit()
    db.delete(settings)
    db.commit()
    return user


@router.patch("/update")
def update_user(user_request: schemas.UserUpdate, settings_request: schemas.UserSettingsUpdate,
                db: Session = Depends(get_db)):
    user = db.get(models.User, user_request.id)
    # if not db_hero:
    #     raise HTTPException(status_code=404, detail="Hero not found")
    user_data = user_request.dict(exclude_unset=True)
    user_settings = db.get(models.UserSettings, user.settings_id)
    user_settings.consumption_is_eu = settings_request.consumption_is_eu
    user_settings.odometer_is_eu = settings_request.odometer_is_eu
    for key, value in user_data.items():
        setattr(user, key, value)
    db.add(user)
    db.add(user_settings)
    db.commit()
    db.refresh(user)
    db.refresh(user_settings)
    return user
