from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import timedelta

from schemas import UserRegister, UserLogin, Token
from repositories import UserRepository
from auth import verify_password, create_access_token
from config import settings


class AuthService:
    """Service for authentication business logic"""
    
    @staticmethod
    def register_user(db: Session, user_data: UserRegister) -> dict:
        """Register a new user"""
        # Check if user already exists
        existing_user = UserRepository.get_user_by_email(db, user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Create user
        user = UserRepository.create_user(db, user_data)
        
        # Generate token
        access_token = create_access_token(
            data={"sub": user.email, "role": user.role.value}
        )
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "role": user.role
            }
        }
    
    @staticmethod
    def login_user(db: Session, login_data: UserLogin) -> dict:
        """Authenticate user and return JWT token"""
        user = UserRepository.get_user_by_email(db, login_data.email)
        
        if not user or not verify_password(login_data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        access_token = create_access_token(
            data={"sub": user.email, "role": user.role.value}
        )
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "role": user.role
            }
        }
    
    @staticmethod
    def forgot_password(db: Session, email: str) -> dict:
        """Mock forgot password flow (no email sending)"""
        user = UserRepository.get_user_by_email(db, email)
        
        if not user:
            # Don't reveal if email exists for security
            return {
                "message": "If the email exists, a password reset link has been sent"
            }
        
        # In a real application, you would:
        # 1. Generate a reset token
        # 2. Send email with reset link
        # 3. Store token in database with expiration
        
        # For this mock implementation, just return success message
        return {
            "message": "If the email exists, a password reset link has been sent",
            "mock_reset_token": "mock-token-12345"  # Only for development
        }

