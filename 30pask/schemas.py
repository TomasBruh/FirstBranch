from pydantic import BaseModel
from typing import Union


class BlogBase(BaseModel):
    title: str
    description: Union[str, None] = None


class BlogCreate(BlogBase):
    pass


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserCreate(UserBase):
    password: str


class HumanShortGetInfoSchema(BaseModel):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class Blog(BlogBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    blogs: list[Blog] = []

    class Config:
        orm_mode = True
# SQLAlchemy and many others are by default "lazy loading". That means, for example, that they don't fetch the data for
# relationships from the database unless you try to access the attribute that would contain that data.
# For example, accessing the attribute items: current_user.items would make SQLAlchemy go to the items table and get the
# items for this user, but not before. Without orm_mode, if you returned a SQLAlchemy model from your path operation, it
# wouldn't include the relationship data. Even if you declared those relationships in your Pydantic models. But with ORM
# mode, as Pydantic itself will try to access the data it needs from attributes (instead of assuming a dict), you can
# declare the specific data you want to return and it will be able to go and get it, even from ORMs.


class UserPostSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
