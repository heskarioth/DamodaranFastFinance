from ..db import models
from .. import schemas
from fastapi import APIRouter, HTTPException, Depends, Response, status
from sqlalchemy.orm import Session
from ..db.database import get_db
from .. import utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(tags=['Authentication'])


@router.post("/login",response_model=schemas.Token)
def login(user_credentials : OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    
    #check if that user exist.
    user = db.query(models.table_users).filter(models.table_users.email==user_credentials.username).first()
    
    if not user:        
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Invalid credentials.')
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail='Invalid credentials.')

    access_token = oauth2.create_access_token(data={'sub':user.email})

    return {"access_token":access_token,"token_type":"bearer"}
