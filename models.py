import pytz
from sqlalchemy import text
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()


class Car(Base):
    __tablename__ = 'car'
    id  = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    car_type = Column(String)
    available_count  = Column(Integer, nullable=False)
    rent_per_day = Column(Float, nullable=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, ForeignKey('user.id'))
    created_by = relationship('User')


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    phone_number = Column(String)
    address = Column(String)
    is_admin = Column(Boolean, default=False)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())


class UserRental(Base):
    __tablename__ = 'user_rental'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    car_id = Column(Integer, ForeignKey('car.id'))
    rented_car_count  = Column(Integer, nullable=False)
    user_requested_duration_in_days  = Column(Integer, nullable=False)
    rental_started = Column(DateTime(timezone=True), server_default=func.now())
    rental_end_date = Column(DateTime(timezone=True), onupdate=func.now())
    total_rent = Column(Float)
    created_by = relationship('User')
    car = relationship('Car')

    def serialize(self):
        rental_data = {
            'id': self.id,
            'user_name': self.created_by.name,
            'user_id': self.user_id,
            'user_email': self.created_by.email,
            'car_id': self.car_id,
            'car_name': self.car.name,
            'car_type': self.car.car_type,
            'rented_car_count': self.rented_car_count,
            'user_requested_duration_in_days': self.user_requested_duration_in_days,
            'rental_started': self.rental_started
        }
        if self.rental_end_date:
            rental_data['rental_end_date'] = self.rental_end_date
            rental_data['total_rent'] = self.total_rent
        return rental_data


