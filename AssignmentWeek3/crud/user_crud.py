from sqlalchemy.orm import Session
from models import User
from schemas import userSchema
from hashing import Hash

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: userSchema.UserRequestCO):
    # Check if user already exists
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        return None
    
    db_user = User(name=user.name, email=user.email, password=Hash.bcrypt(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_users(db: Session):
    return db.query(User).all()

def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user