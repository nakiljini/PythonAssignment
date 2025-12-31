from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from schemas import AppointmentCreate, AppointmentResponse, AvailabilityCreate, AvailabilityResponse
from services import AppointmentService, AvailabilityService
from database import get_db
from auth import get_current_user, get_current_doctor, get_current_patient
from models import User, UserRole

router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=AppointmentResponse)
def create_appointment(
    appointment_data: AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_patient)
):
    """Book an appointment (Patient only)"""
    appointment = AppointmentService.create_appointment(db, appointment_data, current_user)
    return appointment


@router.get("/my-appointments", response_model=List[AppointmentResponse])
def get_my_appointments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get current user's appointments"""
    if current_user.role == UserRole.DOCTOR:
        appointments = AppointmentService.get_doctor_appointments(db, current_user)
    else:
        appointments = AppointmentService.get_patient_appointments(db, current_user)
    return appointments


@router.post("/cancel/{appointment_id}")
def cancel_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_patient)
):
    """Cancel an appointment (Patient only)"""
    return AppointmentService.cancel_appointment(db, appointment_id, current_user)


# Doctor-specific routes
@router.post("/availability", status_code=status.HTTP_201_CREATED, response_model=AvailabilityResponse)
def set_availability(
    availability_data: AvailabilityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_doctor)
):
    """Set availability slots (Doctor only)"""
    availability = AvailabilityService.create_availability(db, availability_data, current_user)
    return availability


@router.get("/upcoming", response_model=List[AppointmentResponse])
def get_upcoming_appointments(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_doctor)
):
    """Get upcoming appointments (Doctor only)"""
    appointments = AppointmentService.get_doctor_appointments(db, current_user)
    return appointments

