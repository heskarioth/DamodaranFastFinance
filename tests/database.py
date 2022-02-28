from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from app.main import app

from app.config import database_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.db.database import get_db, Base
from app.db import models




SQLALCHEMY_DATABASE_URL =f'postgresql://{database_settings.database_username}:{database_settings.database_password}@{database_settings.database_hostname}:{database_settings.database_port}/{database_settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)


@pytest.fixture
def session(): # this is to get the db
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session): 
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    
    

