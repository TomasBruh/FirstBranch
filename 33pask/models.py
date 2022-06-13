from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)

    settings = relationship('UserSettings', back_populates='user')
    settings_id = Column(Integer, ForeignKey('user_settings.id'))


class UserSettings(Base):
    __tablename__ = 'user_settings'

    id = Column(Integer, primary_key=True, index=True)
    consumption_is_eu = Column(Boolean, default=True)
    odometer_is_eu = Column(Boolean, default=True)

    user = relationship('User', back_populates='settings', uselist=False)


class CarBrand(Base):
    __tablename__ = 'car_brands'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    founded_in_year = Column(Integer)

    models = relationship('CarBrandModel', back_populates='brand')  # , uselist =True#


class CarBrandModel(Base):
    __tablename__ = 'car_brand_models'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    # release_date = Column(String)
    # four_wheel_drive = Column(Boolean)

    brand_id = Column(Integer, ForeignKey('car_brands.id'))
    brand = relationship('CarBrand', back_populates='models')
    # cars = relationship('Car', back_populates='brand_model')


# class Car(Base):
#     __tablename__ = 'cars'
#
#     id = Column(Integer, primary_key=True, index=True)
#     mileage = Column(Integer)
#
#     brand_model_id = Column(String, ForeignKey('car_brand_models.id'))
#     brand_model = relationship('CarBrandModel', back_populates='cars')