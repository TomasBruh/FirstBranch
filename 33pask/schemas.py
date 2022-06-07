import datetime
from typing import List, Optional
from pydantic import BaseModel


class UserAll(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    settings_id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserSettingsAll(BaseModel):
    id: int
    user_id: int
    consumption_is_eu: bool
    odometer_is_eu: bool

    class Config:
        orm_mode = True


class UserSettingsCreate(BaseModel):
    consumption_is_eu: bool
    odometer_is_eu: bool


class CarBrandCreate(BaseModel):
    name: str
    founded_in_year: str


class CarBrandModelCreate(BaseModel):
    name: str
    release_date: str
    brand_id: int


class CarBrandModelAll(BaseModel):
    id: int
    name: str
    release_date: str
    brand_id: int


class CarAll(BaseModel):
    id: int
    mileage: int
    brand_model_id: int

    class Config:
        orm_mode = True


class CarCreate(BaseModel):
    mileage: int
    brand_model_id: int


class CarBrandAll(BaseModel):
    id: int
    name: str
    founded_in_year: str
    models: List[CarBrandModelAll] = []

    class Config:
        orm_mode = True



