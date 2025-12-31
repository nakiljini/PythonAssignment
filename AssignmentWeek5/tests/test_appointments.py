import pytest
from fastapi import status
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from models import Availability, Appointment
from services import AppointmentService, AvailabilityService
from schemas import AppointmentCreate, AvailabilityCreate
from repositories import AvailabilityRepository


def test_create_availability(client, test_doctor, db_session: Session):
    """Test doctor creating availability"""
    # Login as doctor
    login_response = client.post(
        "/auth/login",
        json={"email": "doctor@test.com", "password": "password123"}
    )
    token = login_response.json()["access_token"]
    
    # Create availability
    start_time = datetime.utcnow() + timedelta(days=1)
    end_time = start_time + timedelta(hours=2)
    
    availability_data = AvailabilityCreate(
        start_time=start_time.isoformat(),
        end_time=end_time.isoformat()
    )
    
    response = client.post(
        "/appointments/availability",
        json=availability_data.dict(),
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["doctor_id"] == test_doctor.id


def test_get_all_doctors(client, test_doctor):
    """Test getting list of all doctors"""
    response = client.get("/doctors")
    assert response.status_code == status.HTTP_200_OK
    doctors = response.json()
    assert len(doctors) >= 1
    assert any(d["email"] == "doctor@test.com" for d in doctors)


def test_get_doctor_availability(client, test_doctor, db_session: Session):
    """Test getting doctor availability"""
    # Create availability
    start_time = datetime.utcnow() + timedelta(days=1)
    end_time = start_time + timedelta(hours=2)
    
    availability = Availability(
        doctor_id=test_doctor.id,
        start_time=start_time,
        end_time=end_time
    )
    db_session.add(availability)
    db_session.commit()
    
    # Get availability
    response = client.get(f"/doctors/{test_doctor.id}/availability")
    assert response.status_code == status.HTTP_200_OK
    availabilities = response.json()
    assert len(availabilities) >= 1


def test_book_appointment(client, test_doctor, test_patient, db_session: Session):
    """Test patient booking an appointment"""
    # Create availability
    start_time = datetime.utcnow() + timedelta(days=1)
    end_time = start_time + timedelta(hours=2)
    
    availability = Availability(
        doctor_id=test_doctor.id,
        start_time=start_time,
        end_time=end_time
    )
    db_session.add(availability)
    db_session.commit()
    db_session.refresh(availability)
    
    # Login as patient
    login_response = client.post(
        "/auth/login",
        json={"email": "patient@test.com", "password": "password123"}
    )
    token = login_response.json()["access_token"]
    
    # Book appointment
    appointment_time = start_time + timedelta(hours=1)
    appointment_data = AppointmentCreate(
        doctor_id=test_doctor.id,
        availability_id=availability.id,
        appointment_time=appointment_time.isoformat()
    )
    
    response = client.post(
        "/appointments",
        json=appointment_data.dict(),
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["doctor_id"] == test_doctor.id
    assert data["patient_id"] == test_patient.id


def test_double_booking_prevention(client, test_doctor, test_patient, db_session: Session):
    """Test that double booking is prevented"""
    # Create availability
    start_time = datetime.utcnow() + timedelta(days=1)
    end_time = start_time + timedelta(hours=2)
    
    availability = Availability(
        doctor_id=test_doctor.id,
        start_time=start_time,
        end_time=end_time
    )
    db_session.add(availability)
    db_session.commit()
    db_session.refresh(availability)
    
    # Login as patient
    login_response = client.post(
        "/auth/login",
        json={"email": "patient@test.com", "password": "password123"}
    )
    token = login_response.json()["access_token"]
    
    # Book first appointment
    appointment_time = start_time + timedelta(hours=1)
    appointment_data = AppointmentCreate(
        doctor_id=test_doctor.id,
        availability_id=availability.id,
        appointment_time=appointment_time.isoformat()
    )
    
    response1 = client.post(
        "/appointments",
        json=appointment_data.dict(),
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response1.status_code == status.HTTP_201_CREATED
    
    # Try to book same slot again
    response2 = client.post(
        "/appointments",
        json=appointment_data.dict(),
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response2.status_code == status.HTTP_409_CONFLICT
    assert "already booked" in response2.json()["detail"]


def test_cancel_appointment(client, test_doctor, test_patient, db_session: Session):
    """Test patient canceling their appointment"""
    # Create availability and appointment
    start_time = datetime.utcnow() + timedelta(days=1)
    end_time = start_time + timedelta(hours=2)
    
    availability = Availability(
        doctor_id=test_doctor.id,
        start_time=start_time,
        end_time=end_time
    )
    db_session.add(availability)
    db_session.commit()
    db_session.refresh(availability)
    
    appointment = Appointment(
        doctor_id=test_doctor.id,
        patient_id=test_patient.id,
        availability_id=availability.id,
        appointment_time=start_time + timedelta(hours=1),
        status="scheduled"
    )
    db_session.add(appointment)
    db_session.commit()
    db_session.refresh(appointment)
    
    # Login as patient
    login_response = client.post(
        "/auth/login",
        json={"email": "patient@test.com", "password": "password123"}
    )
    token = login_response.json()["access_token"]
    
    # Cancel appointment
    response = client.post(
        f"/appointments/cancel/{appointment.id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == status.HTTP_200_OK
    assert "cancelled" in response.json()["message"].lower()


def test_get_my_appointments(client, test_patient):
    """Test getting current user's appointments"""
    # Login as patient
    login_response = client.post(
        "/auth/login",
        json={"email": "patient@test.com", "password": "password123"}
    )
    token = login_response.json()["access_token"]
    
    # Get appointments
    response = client.get(
        "/appointments/my-appointments",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)

