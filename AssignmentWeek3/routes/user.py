from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from schemas import userSchema
from database import SessionLocal
from crud import user_crud as user_crud

router = APIRouter(prefix="/user", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=userSchema.UserResponseDTO)
def register_user(request: userSchema.UserRequestCO, db: Session = Depends(get_db)):
    user = user_crud.create_user(db, request)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return user

@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=userSchema.UserResponseDTO)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    return user