"""
Database initialization script
Run this to create all database tables
"""
from database import engine, Base
from models import User, Availability, Appointment

if __name__ == "__main__":
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

