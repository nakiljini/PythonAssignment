from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from models import UserRole


# Auth Schemas
class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
    role: UserRole
    name: str = Field(..., min_length=1)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    email: Optional[str] = None
    role: Optional[str] = None


# User Schemas
class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    role: UserRole
    created_at: datetime
    
    class Config:
        from_attributes = True


# Availability Schemas
class AvailabilityCreate(BaseModel):
    start_time: datetime
    end_time: datetime


class AvailabilityResponse(BaseModel):
    id: int
    doctor_id: int
    start_time: datetime
    end_time: datetime
    
    class Config:
        from_attributes = True


# Appointment Schemas
class AppointmentCreate(BaseModel):
    doctor_id: int
    availability_id: int
    appointment_time: datetime


class AppointmentResponse(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    availability_id: int
    appointment_time: datetime
    status: str
    created_at: datetime
    doctor: UserResponse
    patient: UserResponse
    
    class Config:
        from_attributes = True


# Doctor Schemas
class DoctorResponse(BaseModel):
    id: int
    name: str
    email: str
    
    class Config:
        from_attributes = True

