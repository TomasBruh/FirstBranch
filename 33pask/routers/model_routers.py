from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db


router = APIRouter(
    prefix='/api/model',
    tags=['Models']
)


@router.get('/get_all')
def get_all(db: Session = Depends(get_db)):
    return db.query(models.CarModel).all()


@router.post('/create')
def create_model(request: schemas.CarModelCreate, db: Session = Depends(get_db)):
    new_model = models.CarModel(
        name=request.name,
        brand_id=request.brand_id
    )
    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    return new_model


@router.delete('/delete/{model_id}')
def delete_model(model_id: int, db: Session = Depends(get_db)):
    model = db.get(models.CarModel, model_id)
    db.delete(model)
    db.commit()
    return model


@router.patch('/update')
def update_model(request: schemas.CarModelUpdate, db: Session = Depends(get_db)):
    car_model = db.get(models.CarModel, request.id)
    car_model_data = request.dict()
    for key, value in car_model_data.items():
        if key != 'settings':
            setattr(car_model, key, value)

    db.add(car_model)
    db.commit()
    db.refresh(car_model)
    return car_model
