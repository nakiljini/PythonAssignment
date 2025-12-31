from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schemas import UserRegister, UserLogin, ForgotPasswordRequest, Token
from services import AuthService
from database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user_data: UserRegister, db: Session = Depends(get_db)):
    """Register a new user (Doctor or Patient)"""
    return AuthService.register_user(db, user_data)


@router.post("/login", response_model=Token)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    """Login and get JWT token"""
    return AuthService.login_user(db, login_data)


@router.post("/forgot-password")
def forgot_password(request: ForgotPasswordRequest, db: Session = Depends(get_db)):
    """Mock forgot password flow"""
    return AuthService.forgot_password(db, request.email)

