from passlib.context import CryptContext

PEPPER = "dfcgvhbjnkmldwvdsfghhj"
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    @staticmethod
    def bcrypt(password: str) -> str:
        return pwd_cxt.hash(password + PEPPER)

    @staticmethod
    def verify(hashed_user_password: str, plain_request_password: str) -> bool:
        return pwd_cxt.verify(plain_request_password + PEPPER, hashed_user_password)