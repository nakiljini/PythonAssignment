import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from models import Base
from database import engine
from routes import user, authentication

app = FastAPI()

Base.metadata.create_all(engine)

# Include routers
app.include_router(user.router)
app.include_router(authentication.router)

@app.get("/")
def root():
    return {"message": "User Management API"}