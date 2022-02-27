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
    tags=['CashFlow Estimations']
)


@router.get("/working_capital",response_model=List[schemas.schema_wcdata],summary="Working Capital Ratios by Sector")
async def get_wcdata(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_wcdata).all()
    return posts

@router.get("/financing_flows",response_model=List[schemas.schema_finflows],summary="Financing Flows by Sector")
async def get_finflows(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_finflows).all()
    return posts

@router.get("/margin_sector",response_model=List[schemas.schema_margin],summary="Margins by Sector")
async def get_margin(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_margin).all()
    return posts

@router.get("/goodwill",response_model=List[schemas.schema_goodwill],summary="Goodwill Statistics by Sector")
async def get_goodwill(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_goodwill).all()
    return posts


@router.get("/research_and_development",response_model=List[schemas.schema_r_d],summary="R&D Statistics by Sector")
async def get_r_d(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_r_d).all()
    return posts

@router.get("/cap_expenditure",response_model=List[schemas.schema_capex],summary="Capital Expenditures by Sector")
async def get_capex(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_capex).all()
    return posts