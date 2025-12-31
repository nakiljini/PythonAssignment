import pytest
from fastapi import status
from sqlalchemy.orm import Session

from models import User, UserRole
from services import AuthService
from schemas import UserRegister, UserLogin


def test_register_doctor(client, db_session: Session):
    """Test doctor registration"""
    user_data = UserRegister(
        email="doctor@example.com",
        password="password123",
        role=UserRole.DOCTOR,
        name="Dr. Smith"
    )
    
    response = client.post("/auth/register", json=user_data.dict())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert "access_token" in data
    assert data["user"]["email"] == "doctor@example.com"
    assert data["user"]["role"] == "Doctor"


def test_register_patient(client, db_session: Session):
    """Test patient registration"""
    user_data = UserRegister(
        email="patient@example.com",
        password="password123",
        role=UserRole.PATIENT,
        name="John Doe"
    )
    
    response = client.post("/auth/register", json=user_data.dict())
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert "access_token" in data
    assert data["user"]["role"] == "Patient"


def test_register_duplicate_email(client, db_session: Session):
    """Test registration with duplicate email"""
    user_data = UserRegister(
        email="test@example.com",
        password="password123",
        role=UserRole.PATIENT,
        name="Test User"
    )
    
    # First registration
    response1 = client.post("/auth/register", json=user_data.dict())
    assert response1.status_code == status.HTTP_201_CREATED
    
    # Duplicate registration
    response2 = client.post("/auth/register", json=user_data.dict())
    assert response2.status_code == status.HTTP_400_BAD_REQUEST
    assert "already registered" in response2.json()["detail"]


def test_login_success(client, test_patient):
    """Test successful login"""
    login_data = UserLogin(
        email="patient@test.com",
        password="password123"
    )
    
    response = client.post("/auth/login", json=login_data.dict())
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_credentials(client, test_patient):
    """Test login with invalid credentials"""
    login_data = UserLogin(
        email="patient@test.com",
        password="wrongpassword"
    )
    
    response = client.post("/auth/login", json=login_data.dict())
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_forgot_password(client, test_patient):
    """Test forgot password endpoint"""
    response = client.post(
        "/auth/forgot-password",
        json={"email": "patient@test.com"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert "message" in response.json()


def test_forgot_password_nonexistent_email(client):
    """Test forgot password with non-existent email"""
    response = client.post(
        "/auth/forgot-password",
        json={"email": "nonexistent@test.com"}
    )
    assert response.status_code == status.HTTP_200_OK
    # Should not reveal if email exists


def test_password_hashing():
    """Test password hashing and verification"""
    from auth import get_password_hash, verify_password
    
    password = "testpassword123"
    hashed = get_password_hash(password)
    
    assert hashed != password
    assert verify_password(password, hashed)
    assert not verify_password("wrongpassword", hashed)

