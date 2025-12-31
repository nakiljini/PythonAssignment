from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from schemas import tokenSchema

SECRET_KEY = 'ekhdjsokeirhgjkpweforighjawijkmemnjlno83iiem'
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_jwt_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentions_exception):
    try :
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        email: str = payload.get('sub')
        if email is None:
            raise credentions_exception
        token_data = tokenSchema.TokenData(email = email)
    except JWTError:
        raise credentions_exception
    return token_data