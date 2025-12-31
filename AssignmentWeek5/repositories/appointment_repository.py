from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime
from models import Appointment, User


class AppointmentRepository:
    """Repository for appointment database operations"""
    
    @staticmethod
    def create_appointment(
        db: Session,
        doctor_id: int,
        patient_id: int,
        availability_id: int,
        appointment_time: datetime
    ) -> Appointment:
        """Create a new appointment"""
        appointment = Appointment(
            doctor_id=doctor_id,
            patient_id=patient_id,
            availability_id=availability_id,
            appointment_time=appointment_time,
            status="scheduled"
        )
        db.add(appointment)
        db.commit()
        db.refresh(appointment)
        return appointment
    
    @staticmethod
    def get_appointment_by_id(db: Session, appointment_id: int) -> Optional[Appointment]:
        """Get appointment by ID"""
        return db.query(Appointment).filter(Appointment.id == appointment_id).first()
    
    @staticmethod
    def get_doctor_appointments(
        db: Session,
        doctor_id: int,
        upcoming_only: bool = True
    ) -> List[Appointment]:
        """Get all appointments for a doctor"""
        query = db.query(Appointment).filter(Appointment.doctor_id == doctor_id)
        
        if upcoming_only:
            query = query.filter(Appointment.appointment_time >= datetime.utcnow())
        
        return query.order_by(Appointment.appointment_time).all()
    
    @staticmethod
    def get_patient_appointments(
        db: Session,
        patient_id: int,
        upcoming_only: bool = True
    ) -> List[Appointment]:
        """Get all appointments for a patient"""
        query = db.query(Appointment).filter(Appointment.patient_id == patient_id)
        
        if upcoming_only:
            query = query.filter(Appointment.appointment_time >= datetime.utcnow())
        
        return query.order_by(Appointment.appointment_time).all()
    
    @staticmethod
    def check_double_booking(
        db: Session,
        doctor_id: int,
        appointment_time: datetime,
        availability_id: int
    ) -> bool:
        """Check if there's already an appointment at this time"""
        return db.query(Appointment).filter(
            Appointment.doctor_id == doctor_id,
            Appointment.availability_id == availability_id,
            Appointment.status == "scheduled"
        ).first() is not None
    
    @staticmethod
    def cancel_appointment(db: Session, appointment_id: int, user_id: int) -> Optional[Appointment]:
        """Cancel an appointment (patient can cancel their own)"""
        appointment = db.query(Appointment).filter(
            Appointment.id == appointment_id,
            Appointment.patient_id == user_id
        ).first()
        
        if appointment:
            appointment.status = "cancelled"
            db.commit()
            db.refresh(appointment)
        
        return appointment

