# essential routes
    # Cost of Equity
    # Beta    
#from http.client import responses
from numpy import size
from ..db import models
from fastapi import Body,Response, status,HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..db.database import get_db
from sqlalchemy import func
from typing import List
from .. import schemas
from app.db.etl.jobs.etl_reference_items import f_ref_industry_names

router = APIRouter(
    prefix = "/reference_items"
    ,tags = ["Essentials"]
    
)
#@router.get("/{ticker}", response_model=List[schemas.IndustryNameOut])
@router.get("/{ticker}")
def get_industry_group(ticker : str, db : Session = Depends(get_db)):
    #tick = db.query(models.table_ref_industry_names).filter(models.table_ref_industry_names.ticker==ticker.upper()).all()
    df = f_ref_industry_names("")
    if size(df[df['ticker']==ticker.upper()])==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Ticker {} not found'.format(ticker))
    tick = df[df['ticker']==ticker.upper()].to_dict(orient='records')[0]
    return tick

