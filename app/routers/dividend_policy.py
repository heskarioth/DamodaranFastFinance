#from http.client import responses
from ..db import models
from fastapi import Body, FastAPI, Response, status,HTTPException, Depends, APIRouter, Query
from sqlalchemy.orm import Session
from ..db.database import get_db
from sqlalchemy import func
from typing import List, Optional
from .. import schemas

router = APIRouter(
    #prefix="/discount_rates"
    tags=['Dividend Policy']
)

@router.get("/dividends_fcfe",response_model=List[schemas.schema_divfcfe],summary="Dividends and FCFE by Sector")
async def get_divfcfe(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_divfcfe).all()
    return posts

@router.get("/dividends_fundamentals",response_model=List[schemas.schema_divfund],summary="Dividend Fundamentals by Sector")
async def get_divfund(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_divfund).all()
    return posts

