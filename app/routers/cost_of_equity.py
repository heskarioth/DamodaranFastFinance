from http.client import responses
from ..db import models
from fastapi import Body, FastAPI, Response, status,HTTPException, Depends, APIRouter, Query
from sqlalchemy.orm import Session
from ..db.database import get_db
from sqlalchemy import func
from typing import List, Optional
from .. import schemas
from .. import oauth2
# buttons one of swagger ui params: https://fastapi.tiangolo.com/advanced/extending-openapi/



router = APIRouter(
    #prefix="/discount_rates"
    tags=['Cost of Equity']
)


@router.get("/betas/sector_betas",response_model=List[schemas.schema_betas],summary="Betas by Sector")
async def get_betas(db: Session = Depends(get_db),current_user : int = Depends(oauth2.get_current_user)):
    posts = db.query(models.table_betas).all()
    return posts
    
@router.get("/betas/sector_betas_private",summary="Total Betas by Sector (for computing private company costs of equity)")
async def get_totalbeta(db: Session = Depends(get_db)):
    """
    summary_documentation = https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/
    """
    posts = db.query(models.table_totalbeta).all()
    return posts
@router.get("/wacc",response_model=List[schemas.schema_wacc],summary="Cost of Equity and Capital By Sector")
async def get_wacc(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_wacc).all()
    return posts

@router.get("/tax/corporate_tax",response_model=List[schemas.schema_countrytaxrates],summary="Corporate Marginal Tax Rates - By country")
async def get_countrytaxrates(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_countrytaxrates).all()
    return posts

@router.get("/tax/taxrate",response_model=List[schemas.schema_taxrate],summary="Tax Rates by Sector")
async def get_taxrate(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_taxrate).all()
    return posts

@router.get("/risk/cds_risk_premiums",response_model=List[schemas.schema_ctryprem],summary="Country Default Spreads and Risk Premiums")
async def get_ctryprem(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_ctryprem).all()
    return posts

@router.get("/risk/historical_erp",response_model=List[schemas.schema_histimpl],summary="Historical Implied Equity Risk Premiums")
async def get_histimpl(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_histimpl).all()
    return posts

@router.get("/historical_returns",response_model=List[schemas.schema_histretSP],summary="Historical Returns on Stocks, Bonds and Bills: 1928-2021")
async def get_histretSP(db: Session = Depends(get_db)):
    """
    placeholder text
    """
    posts = db.query(models.table_histretSP).all()
    return posts



# @router.get("/riskrates/riskfree_rates",tags=['xx'])
# async def get_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.table_macro).all()
#     return posts

# @router.get(
#     "/riskpremiums"
    
#     ,responses={
#         403: {"description": "Operation forbidden"}
#         }
# )
# async def get_posts(
#         db: Session = Depends(get_db)
#         ,query_para : int = 0
#         ,query_param_1: float = Query(None, description="description goes here", )
#         ,query_param_2: float = Query(None, description="Param 2 does xyz")
# ):
#     posts = db.query(models.table_macro).all()
#     return posts


