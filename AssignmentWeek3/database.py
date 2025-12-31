from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

password = quote_plus('Root@23')
SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://root:{password}@localhost:3306/user_management_db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()