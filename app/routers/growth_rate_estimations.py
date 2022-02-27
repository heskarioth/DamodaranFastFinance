from http.client import responses
from ..db import models
from fastapi import FastAPI, Response, status,HTTPException, Depends, APIRouter, Query
from sqlalchemy.orm import Session
from ..db.database import get_db
#from sqlalchemy import func
from typing import List
from .. import schemas


router = APIRouter(
    #prefix="/discount_rates"
    tags=['Growth Rate Estimations']
)


@router.get("/return_on_equity",response_model=List[schemas.schema_roe],summary="Return on Equity by Sector")
#@router.get("/return_on_equity",summary="Return on Equity by Sector")
async def get_roe(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_roe).all()
    return posts

@router.get("/eps_growth",response_model=List[schemas.schema_fundgr],summary="Fundamental Growth in EPS by Sector")
async def get_fundgr(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_fundgr).all()
    return posts

@router.get("/hist_comp_growth",response_model=List[schemas.schema_histgr],summary="Historical (Compounded Annual) Growth Rates by Sector")
async def get_histgr(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_histgr).all()
    return posts

@router.get("/growth_ebit",response_model=List[schemas.schema_fundgrEB],summary="Fundamental Growth in EBIT by Sector (US)")
async def get_fundgrEB(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_fundgrEB).all()
    return posts