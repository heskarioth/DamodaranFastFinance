from http.client import responses
from ..db import models
from fastapi import Body, FastAPI, Response, status,HTTPException, Depends, APIRouter, Query
from sqlalchemy.orm import Session
from ..db.database import get_db
from sqlalchemy import func
from typing import List, Optional
from .. import schemas

router = APIRouter(
    #prefix="/discount_rates"
    tags=['Capital Structure']
)


@router.get("/macro",response_model=List[schemas.schema_macro],summary="Macro Economic Data - Annual")
async def get_macro(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_macro).all()
    return posts

@router.get("/debt_fundamentals",response_model=List[schemas.schema_dbtfund],summary="Debt Fundamentals by Sector")
async def get_dbtfund(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_dbtfund).all()
    return posts

@router.get("/debt_details",response_model=List[schemas.schema_debtdetails],summary="Debt Details by Sector")
async def get_debtdetails(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_debtdetails).all()
    return posts


@router.get("/lease_effect",response_model=List[schemas.schema_leaseeffect],summary="Lease Effect on Debt and Profitability by Sector")
#@router.get("/lease_effect",summary="Lease Effect on Debt and Profitability by Sector")
async def get_leaseeffect(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_leaseeffect).all()
    return posts


