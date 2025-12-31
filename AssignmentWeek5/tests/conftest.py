import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app
from database import Base, get_db
from models import User, UserRole
from auth import get_password_hash


# Test database (SQLite in-memory)
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def db_session():
    """Create a fresh database for each test"""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """Create a test client"""
    return TestClient(app)


@pytest.fixture
def test_doctor(db_session):
    """Create a test doctor user"""
    doctor = User(
        email="doctor@test.com",
        password_hash=get_password_hash("password123"),
        role=UserRole.DOCTOR,
        name="Dr. Test"
    )
    db_session.add(doctor)
    db_session.commit()
    db_session.refresh(doctor)
    return doctor


@pytest.fixture
def test_patient(db_session):
    """Create a test patient user"""
    patient = User(
        email="patient@test.com",
        password_hash=get_password_hash("password123"),
        role=UserRole.PATIENT,
        name="Patient Test"
    )
    db_session.add(patient)
    db_session.commit()
    db_session.refresh(patient)
    return patient

