from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db

router = APIRouter(
    prefix='/api/brand',
    tags=['Brands']
)


@router.get('')
def get_all(db: Session = Depends(get_db)):
    brands = db.query(models.CarBrand).all()
    for brand in brands:
        _ = brand.models
    return brands


@router.post('/create')
def create_brand(request: schemas.CarBrandCreate, db: Session = Depends(get_db)):
    new_brand = models.CarBrand(
        name=request.name,
        founded_in_year=request.founded_in_year
    )
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)

    return new_brand


@router.patch("/update") # {brand_id}??????????????????????
def update_car_brand(request: schemas.CarBrandUpdate, db: Session = Depends(get_db)):
    car_brand = db.get(models.CarBrand, request.id)
    car_brand_data = request.dict()
    for key, value in car_brand_data.items():
        if key != 'settings':
            setattr(car_brand, key, value)
    _ = car_brand.models
    db.add(car_brand)
    db.commit()
    db.refresh(car_brand)
    return car_brand


@router.delete("/delete/{brand_id}")
def delete_car_brand(brand_id: int, db: Session = Depends(get_db)):
    car_brand = db.get(models.CarBrand, brand_id)
    # if not hero:
    #     raise HTTPException(status_code=404, detail="Hero not found")
    db.delete(car_brand)
    db.commit()
    return car_brand

