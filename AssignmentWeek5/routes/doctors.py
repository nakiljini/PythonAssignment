from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from schemas import DoctorResponse, AvailabilityResponse
from services import AvailabilityService
from repositories import UserRepository
from database import get_db
from auth import get_current_user
from models import User

router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.get("", response_model=List[DoctorResponse])
def get_all_doctors(db: Session = Depends(get_db)):
    """Get list of all doctors (public endpoint)"""
    doctors = UserRepository.get_all_doctors(db)
    return doctors


@router.get("/{doctor_id}/availability", response_model=List[AvailabilityResponse])
def get_doctor_availability(doctor_id: int, db: Session = Depends(get_db)):
    """Get availability slots for a specific doctor (public endpoint)"""
    availabilities = AvailabilityService.get_doctor_availability(db, doctor_id)
    return availabilities

