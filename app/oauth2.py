from pyexpat import model
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import schemas
from app.db import database, models
from .config import other_settings
from sqlalchemy.orm import Session
SECRET_KEY = other_settings.secret_key
ALGORITHM = other_settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = other_settings.access_token_expire_minutes


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def create_access_token(data :dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})

    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentials_exceptions):

    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        email : str = payload.get("sub")
        if email is None:
            raise credentials_exceptions

        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exceptions
    
    return token_data


def get_current_user(token: str = Depends(oauth2_scheme),db: Session = Depends(database.get_db)):
    credentails_exceptions = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
            ,detail="Could not validate credentials"
            ,headers={"WWWW-Authenticate" : "Bearer"}
    )

    token = verify_access_token(token,credentails_exceptions)

    user = db.query(models.table_users).filter(models.table_users.email==token.email).first()

    return user

