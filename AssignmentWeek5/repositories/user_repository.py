from sqlalchemy.orm import Session
from typing import Optional
from models import User, UserRole
from schemas import UserRegister
from auth import get_password_hash


class UserRepository:
    """Repository for user database operations"""
    
    @staticmethod
    def create_user(db: Session, user_data: UserRegister) -> User:
        """Create a new user"""
        hashed_password = get_password_hash(user_data.password)
        db_user = User(
            email=user_data.email,
            password_hash=hashed_password,
            role=user_data.role,
            name=user_data.name
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_all_doctors(db: Session) -> list[User]:
        """Get all users with Doctor role"""
        return db.query(User).filter(User.role == UserRole.DOCTOR).all()
    
    @staticmethod
    def update_password(db: Session, user: User, new_password: str) -> User:
        """Update user password (for forgot password flow)"""
        user.password_hash = get_password_hash(new_password)
        db.commit()
        db.refresh(user)
        return user

