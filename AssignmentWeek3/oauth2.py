from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt_utils
from crud import user_crud
from sqlalchemy.orm import Session
from database import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentails_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                          detail="Could not validate credentails",
                                          headers = {"WWW-Authenticate": "Bearer"}
                                          )
    token_data = jwt_utils.verify_token(token=token, credentions_exception=credentails_exception)
    if token_data is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    user = user_crud.get_user_by_email(db, token_data.email)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    return user
