from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime

from schemas import AppointmentCreate, AvailabilityCreate
from repositories import (
    AppointmentRepository,
    AvailabilityRepository,
    UserRepository
)
from models import User


class AppointmentService:
    """Service for appointment business logic"""
    
    @staticmethod
    def create_appointment(
        db: Session,
        appointment_data: AppointmentCreate,
        patient: User
    ) -> dict:
        """Create a new appointment with validation"""
        # Validate doctor exists
        doctor = UserRepository.get_user_by_id(db, appointment_data.doctor_id)
        if not doctor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doctor not found"
            )
        
        # Validate availability exists and belongs to doctor
        availability = AvailabilityRepository.get_availability_by_id(
            db, appointment_data.availability_id
        )
        if not availability:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Availability slot not found"
            )
        
        if availability.doctor_id != appointment_data.doctor_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Availability does not belong to the specified doctor"
            )
        
        # Check if appointment time is within availability window
        if not (availability.start_time <= appointment_data.appointment_time <= availability.end_time):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Appointment time must be within availability window"
            )
        
        # Check for double booking
        if AppointmentRepository.check_double_booking(
            db,
            appointment_data.doctor_id,
            appointment_data.appointment_time,
            appointment_data.availability_id
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="This time slot is already booked"
            )
        
        # Create appointment
        appointment = AppointmentRepository.create_appointment(
            db,
            appointment_data.doctor_id,
            patient.id,
            appointment_data.availability_id,
            appointment_data.appointment_time
        )
        
        return appointment
    
    @staticmethod
    def cancel_appointment(db: Session, appointment_id: int, patient: User) -> dict:
        """Cancel an appointment"""
        appointment = AppointmentRepository.cancel_appointment(
            db, appointment_id, patient.id
        )
        
        if not appointment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Appointment not found or you don't have permission to cancel it"
            )
        
        return {"message": "Appointment cancelled successfully", "appointment": appointment}
    
    @staticmethod
    def get_doctor_appointments(db: Session, doctor: User) -> list:
        """Get all upcoming appointments for a doctor"""
        appointments = AppointmentRepository.get_doctor_appointments(
            db, doctor.id, upcoming_only=True
        )
        return appointments
    
    @staticmethod
    def get_patient_appointments(db: Session, patient: User) -> list:
        """Get all appointments for a patient"""
        appointments = AppointmentRepository.get_patient_appointments(
            db, patient.id, upcoming_only=False
        )
        return appointments


class AvailabilityService:
    """Service for availability business logic"""
    
    @staticmethod
    def create_availability(
        db: Session,
        availability_data: AvailabilityCreate,
        doctor: User
    ) -> dict:
        """Create availability slot for a doctor"""
        # Validate time range
        if availability_data.start_time >= availability_data.end_time:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Start time must be before end time"
            )
        
        # Check for overlapping availabilities
        if AvailabilityRepository.check_overlapping_availability(
            db,
            doctor.id,
            availability_data.start_time,
            availability_data.end_time
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="This time slot overlaps with existing availability"
            )
        
        availability = AvailabilityRepository.create_availability(
            db,
            doctor.id,
            availability_data.start_time,
            availability_data.end_time
        )
        
        return availability
    
    @staticmethod
    def get_doctor_availability(db: Session, doctor_id: int) -> list:
        """Get all availability slots for a doctor"""
        # Validate doctor exists
        doctor = UserRepository.get_user_by_id(db, doctor_id)
        if not doctor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doctor not found"
            )
        
        availabilities = AvailabilityRepository.get_doctor_availabilities(
            db, doctor_id, start_date=datetime.utcnow()
        )
        return availabilities

