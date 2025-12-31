from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import datetime
from models import Availability, User


class AvailabilityRepository:
    """Repository for availability database operations"""
    
    @staticmethod
    def create_availability(
        db: Session,
        doctor_id: int,
        start_time: datetime,
        end_time: datetime
    ) -> Availability:
        """Create a new availability slot"""
        availability = Availability(
            doctor_id=doctor_id,
            start_time=start_time,
            end_time=end_time
        )
        db.add(availability)
        db.commit()
        db.refresh(availability)
        return availability
    
    @staticmethod
    def get_availability_by_id(db: Session, availability_id: int) -> Optional[Availability]:
        """Get availability by ID"""
        return db.query(Availability).filter(Availability.id == availability_id).first()
    
    @staticmethod
    def get_doctor_availabilities(
        db: Session,
        doctor_id: int,
        start_date: Optional[datetime] = None
    ) -> List[Availability]:
        """Get all availabilities for a doctor"""
        query = db.query(Availability).filter(Availability.doctor_id == doctor_id)
        
        if start_date:
            query = query.filter(Availability.start_time >= start_date)
        
        return query.order_by(Availability.start_time).all()
    
    @staticmethod
    def check_overlapping_availability(
        db: Session,
        doctor_id: int,
        start_time: datetime,
        end_time: datetime,
        exclude_id: Optional[int] = None
    ) -> bool:
        """Check if there's an overlapping availability"""
        query = db.query(Availability).filter(
            Availability.doctor_id == doctor_id,
            Availability.start_time < end_time,
            Availability.end_time > start_time
        )
        
        if exclude_id:
            query = query.filter(Availability.id != exclude_id)
        
        return query.first() is not None

