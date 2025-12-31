import pytest
from fastapi import status
from datetime import datetime, timedelta


def test_doctor_only_endpoints(client, test_doctor, test_patient):
    """Test that doctor-only endpoints require doctor role"""
    # Login as patient
    patient_login = client.post(
        "/auth/login",
        json={"email": "patient@test.com", "password": "password123"}
    )
    patient_token = patient_login.json()["access_token"]
    
    # Try to access doctor-only endpoint
    availability_data = {
        "start_time": (datetime.utcnow() + timedelta(days=1)).isoformat(),
        "end_time": (datetime.utcnow() + timedelta(days=1, hours=2)).isoformat()
    }
    
    response = client.post(
        "/appointments/availability",
        json=availability_data,
        headers={"Authorization": f"Bearer {patient_token}"}
    )
    
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Doctor access required" in response.json()["detail"]


def test_patient_only_endpoints(client, test_doctor):
    """Test that patient-only endpoints require patient role"""
    # Login as doctor
    doctor_login = client.post(
        "/auth/login",
        json={"email": "doctor@test.com", "password": "password123"}
    )
    doctor_token = doctor_login.json()["access_token"]
    
    # Try to access patient-only endpoint (booking appointment)
    appointment_data = {
        "doctor_id": test_doctor.id,
        "availability_id": 1,
        "appointment_time": (datetime.utcnow() + timedelta(days=1)).isoformat()
    }
    
    response = client.post(
        "/appointments",
        json=appointment_data,
        headers={"Authorization": f"Bearer {doctor_token}"}
    )
    
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert "Patient access required" in response.json()["detail"]


def test_protected_endpoints_require_auth(client):
    """Test that protected endpoints require authentication"""
    response = client.get("/appointments/my-appointments")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_public_endpoints_no_auth(client, test_doctor):
    """Test that public endpoints don't require authentication"""
    response = client.get("/doctors")
    assert response.status_code == status.HTTP_200_OK
    
    response = client.get(f"/doctors/{test_doctor.id}/availability")
    assert response.status_code == status.HTTP_200_OK

