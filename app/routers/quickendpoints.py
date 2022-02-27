from curses.ascii import isdigit
from ..db import models
from fastapi import Body,Response, status,HTTPException, Depends, APIRouter, Query
from sqlalchemy.orm import Session
from ..db.database import get_db
from sqlalchemy import func
from typing import List, Optional
from sqlalchemy import func
from .. import schemas
from . import docs
import pandas as pd
import numpy as np
import yfinance as yf

router = APIRouter(
    prefix = "/summary"
    ,tags = ["Quick Enpoints"]
    
)


@router.get(
    "/bottom_up_beta/{industry_group}"
    ,summary="Find industry bottom up beta for industry"
    ,description=docs.bottom_up_beta_industry)
async def get_bottom_up_beta_industry(industry_group: str, db: Session = Depends(get_db)):
    
    if industry_group.isdigit():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Expecting string value')

    betas = db.query(
        models.table_betas.unlevered_beta_corrected_for_cash,
        models.table_betas.effective_tax_rate_percentage,
        models.table_betas.debt_to_equity_ratio_percentage,
        ).filter(models.table_betas.industry_name==industry_group).first()
    
    if not betas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    bottom_up_levered_beta = (betas.unlevered_beta_corrected_for_cash * (1 + ((1- betas.effective_tax_rate_percentage)* betas.debt_to_equity_ratio_percentage)))

    return {'original_data':betas,'calculated_data':{'bottom_up_levered_beta':bottom_up_levered_beta}}
    
@router.get("/bottom_up_beta/",summary="Find firm bottom up beta for firm(s)")
async def get_bottom_up_beta_firm(firm_ticker: list[str] | None = Query(None), db: Session = Depends(get_db)):
#async def get_ctryprem(firm_ticker: str, db: Session = Depends(get_db)):
    """
    Similarly to above, we return bottom up beta. This time using firms debt to equity ratio. I have used YahooAPIs to get firm total debt and market cap. <br>
    You can include multiple firms at the same time.
    """
    firm_ticker = list(set(firm_ticker)) #if user inputs two or more times same ticker
    firm_ticker = [firm.upper() for firm in firm_ticker]
    betas = db.query(
        models.table_ref_industry_names.ticker,
        models.table_ref_industry_names.industry_group,
        models.table_betas.unlevered_beta_corrected_for_cash,
        models.table_betas.effective_tax_rate_percentage,
        models.table_betas.debt_to_equity_ratio_percentage,
        models.table_ref_industry_names.country,

    ).join(
            models.table_ref_industry_names
            ,models.table_betas.industry_name==models.table_ref_industry_names.industry_group
            ).filter(models.table_ref_industry_names.ticker.in_(firm_ticker)).all()
    if not betas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Couldn't find tickers requested")

    
    # https://stackoverflow.com/questions/51453844/find-value-in-a-list-of-dictionaries-without-iterating
    # turning list of tuples to dict [(val,val,val)] -> {key:(val,val),key:(val,val)}
    my_dict = {x[0]:x[2:4] for x in betas}

    # this function can be rewritten to check values saved in database and use those if not older than 1 month
    calculated_data = []
    for firm in firm_ticker:
        ticker = yf.Ticker(firm).info
        total_debt = ticker['totalDebt']
        total_market_cap =  ticker['marketCap']
        debt_to_equity =  total_debt / total_market_cap
        unlevered_beta =  my_dict[firm][0]
        tax_rate = my_dict[firm][1]
        bottom_up_levered_beta = unlevered_beta * (1 + ((1-tax_rate)*debt_to_equity))
        calculated_data.append({'ticker':firm,'total_debt':total_debt,'total_market_cap':total_market_cap,'debt_to_equity':debt_to_equity,'bottom_up_levered_beta':bottom_up_levered_beta})

    return {"original_data":betas,"calculated_data":calculated_data}




@router.get("/risk_premiums/",summary="Find risk premium for the country your firm operates in")
async def get_risk_premium(country_name : Optional[str] = "",db:Session = Depends(get_db)):

    if country_name.isdigit():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Expecting string value.')

    risk_premium = db.query(
        models.table_ctryprem.country,
        models.table_ctryprem.country_risk_premium,
        models.table_ctryprem.equity_risk_premium,
        models.table_ctryprem.adj_default_spread,
        ).filter(func.lower(models.table_ctryprem.country).contains(func.lower(country_name))).all()
    
    if not risk_premium:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    bond = db.query(
        models.table_ref_bonds.country,
        models.table_ref_bonds.yield_converted
        ).filter(func.lower(models.table_ref_bonds.country).contains(func.lower(country_name.strip()))).all()

    bond_dict = dict(bond)
    risk_dict = {x[0]:x[1:] for x in risk_premium}
    calculated_data = []
    for key in risk_dict:
        country_name_lowercase = (key.strip().lower().replace(' ',''))
        try:
            yield_converted = bond_dict[country_name_lowercase]
        except KeyError as k:
            yield_converted = 0
            print('It failed bacause we dont have a bond rate for that country.')
            print('This needs to be fixed in future versions.')

        risk_free = np.abs(yield_converted - risk_dict[key][2])
        calculated_data.append({'country':key,'bond_yield':yield_converted,'risk_free_rate':risk_free})
    

    return {"original_data":risk_premium,"calculated_data":calculated_data}