import sqlalchemy
from ..db import models
from .. import schemas 
from fastapi import APIRouter, HTTPException, Depends, Response, status
from sqlalchemy.orm import Session
from ..db.database import get_db
from .. import utils
from psycopg2.errors import UniqueViolation

router = APIRouter(prefix="/users",tags=['Users'])

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserCreateOut)
def create_user(user : schemas.UserCreate,db: Session = Depends(get_db)):
    #hash the password
    hashed_pwd = utils.hash(user.password)
    user.password = hashed_pwd #replace password with hashed one
    new_user = models.table_users(**user.dict())
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
        return new_user
    except sqlalchemy.exc.IntegrityError as err:
        if isinstance(err.orig,UniqueViolation):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f'User with email: {user.email} already signed up.')


    
