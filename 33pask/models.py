import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from database import Base
from sqlalchemy.orm import relationship
# ID BASE?????????????????


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)

    settings = relationship('UserSettings', back_populates='user')
    settings_id = Column(Integer, ForeignKey('user_settings.id'))

    cars = relationship('Car', back_populates='user')


class UserSettings(Base):
    __tablename__ = 'user_settings'

    id = Column(Integer, primary_key=True, index=True)
    consumption_is_eu = Column(Boolean, default=True)
    odometer_is_eu = Column(Boolean, default=True)

    user = relationship('User', back_populates='settings', uselist=False)


class CarBrand(Base):
    __tablename__ = 'car_brands'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    founded_in_year = Column(Integer)

    models = relationship('CarModel', back_populates='brand')  # , uselist =True#
    cars = relationship('Car', back_populates='brand')


class CarModel(Base):
    __tablename__ = 'car_models'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    # release_date = Column(String)
    # four_wheel_drive = Column(Boolean)

    brand_id = Column(Integer, ForeignKey('car_brands.id'))
    brand = relationship('CarBrand', back_populates='models')

    cars = relationship('Car', back_populates='model')


class CarMileage(Base):
    __tablename__ = 'car_mileage'

    id = Column(Integer, primary_key=True, index=True)
    distance = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now())
    car_id = Column(Integer, ForeignKey('cars.id'))
    car = relationship('Car', back_populates='mileage')


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    mileage = relationship('CarMileage', back_populates='car')

    brand = relationship('CarBrand', back_populates='cars')
    brand_id = Column(Integer, ForeignKey('car_brands.id'))

    model = relationship('CarModel', back_populates='cars')
    model_id = Column(Integer, ForeignKey('car_models.id'))

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='cars')
