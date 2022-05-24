from typing import List, Optional
from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str


class ProductCreate(BaseModel):
    name: str
    category_id: int


class ProductAll(BaseModel):
    id: int
    name: str
    category_id: int

    class Config:
        orm_mode = True


class CategoryAll(BaseModel):
    id: int
    name: str
    products: List[ProductAll] = []

    class Config:
        orm_mode = True

