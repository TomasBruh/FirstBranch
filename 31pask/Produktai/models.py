from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from database import Base
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    products = relationship('Product', back_populates='category')


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')
