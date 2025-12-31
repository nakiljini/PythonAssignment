from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from schemas import userSchema
from database import SessionLocal
from crud import user_crud as user_crud
from hashing import Hash
from jwt_utils import create_jwt_token
from oauth2 import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Authentication"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_crud.get_user_by_email(db, email=request.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    access_token = create_jwt_token(data={'sub': user.email})
    return {'access_token': access_token, "token_type": "bearer"}

@router.get("/current-user", response_model=userSchema.UserResponseDTO)
def get_current_user_endpoint(current_user = Depends(get_current_user)):
    return current_user