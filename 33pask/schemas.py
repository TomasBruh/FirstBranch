from typing import List
from pydantic import BaseModel


class OrmBaseModel(BaseModel):
    class Config:
        orm_mode: True


class UserSettingsAll(OrmBaseModel):
    id: int
    user_id: int
    consumption_is_eu: bool
    odometer_is_eu: bool


class UserSettingsCreate(BaseModel):
    consumption_is_eu: bool
    odometer_is_eu: bool


class UserSettingsUpdate(BaseModel):
    consumption_is_eu: bool
    odometer_is_eu: bool


class UserAll(OrmBaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    settings: UserSettingsAll


class UserAndSettingsCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    settings: UserSettingsCreate


class UserAndSettingsUpdate(OrmBaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    settings: UserSettingsUpdate


class CarModelCreate(BaseModel):
    name: str
    # release_date: str
    brand_id: int


class CarModelAll(BaseModel):
    id: int
    name: str
    # release_date: str
    brand_id: int


class CarModelUpdate(CarModelAll):
    pass


class CarBrandCreate(BaseModel):
    name: str
    founded_in_year: int


class CarBrandAll(OrmBaseModel):
    id: int
    name: str
    founded_in_year: int
    models: List[CarModelAll] = []


class CarBrandUpdate(CarBrandCreate):
    id: int


class CarAll(OrmBaseModel):
    id: int
    brand_id: int
    model_id: int
    user_id: int


class CarCreate(BaseModel):
    brand_id: int
    model_id: int
    user_id: int


class CarUpdate(CarAll):
    pass


class CarMileageCreate(BaseModel):
    distance: int
    car_id: int


class CarMileageAll(BaseModel):
    id: int
    distance: int
    car_id: int
    created_at: str


class CarMileageUpdate(CarMileageCreate):
    id: int
