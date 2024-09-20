from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime, timezone

class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String, unique=True, index=True, nullable=False)

    users = relationship("User", back_populates="role")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role_id = Column(Integer, ForeignKey("user_roles.id"), nullable=False)

    role = relationship("UserRole", back_populates="users")
    appointments = relationship("Appointment", foreign_keys="Appointment.client_id", back_populates="client")
    appointments_as_employee = relationship("Appointment", foreign_keys="Appointment.employee_id", back_populates="employee")
    ratings = relationship("Rating", foreign_keys="Rating.client_id", back_populates="client")

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    employee_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(DateTime, default=datetime.now(timezone.utc))

    client = relationship("User", foreign_keys=[client_id], back_populates="appointments")
    employee = relationship("User", foreign_keys=[employee_id])
    rating = relationship("Rating", back_populates="appointment", uselist=False)

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    appointment_id = Column(Integer, ForeignKey("appointments.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)

    appointment = relationship("Appointment", back_populates="rating")
    client = relationship("User", foreign_keys=[client_id], back_populates="ratings")
