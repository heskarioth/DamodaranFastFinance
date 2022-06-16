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
import re
# on heroku, if I call PG for bottom_up_beta individual firm. I get duplicated  responses.
# 2022-02-27T23:19:09.807129+00:00 app[web.1]: inhold
# 2022-02-27T23:19:09.826004+00:00 app[web.1]: wcdata
# 2022-02-27T23:19:09.850650+00:00 app[web.1]: finflows
# 2022-02-27T23:19:09.883169+00:00 app[web.1]: histimpl
# 2022-02-27T23:19:09.915507+00:00 app[web.1]: margin
# 2022-02-27T23:19:09.934934+00:00 app[web.1]: goodwill
# 2022-02-27T23:19:09.963526+00:00 app[web.1]: r_d
# 2022-02-27T23:19:09.993914+00:00 app[web.1]: capex
# 2022-02-27T23:19:10.016051+00:00 app[web.1]: divfcfe
# 2022-02-27T23:19:10.030702+00:00 app[web.1]: macro
# 2022-02-27T23:19:10.053110+00:00 app[web.1]: dbtfund
# 2022-02-27T23:19:10.073614+00:00 app[web.1]: debtdetails
# 2022-02-27T23:19:10.102485+00:00 app[web.1]: leaseeffect
# 2022-02-27T23:19:10.124543+00:00 app[web.1]: dbtfund
# 2022-02-27T23:19:10.137445+00:00 app[web.1]: wacc
# 2022-02-27T23:19:10.156995+00:00 app[web.1]: debtdetails
# 2022-02-27T23:19:10.157941+00:00 app[web.1]: totalbeta
# 2022-02-27T23:19:10.195422+00:00 app[web.1]: ctryprem
# 2022-02-27T23:19:10.197394+00:00 app[web.1]: leaseeffect
# 2022-02-27T23:19:10.222375+00:00 app[web.1]: betas
# 2022-02-27T23:19:10.227521+00:00 app[web.1]: wacc
# 2022-02-27T23:19:10.245605+00:00 app[web.1]: countrytaxrates
# 2022-02-27T23:19:10.246663+00:00 app[web.1]: totalbeta
# 2022-02-27T23:19:10.270897+00:00 app[web.1]: taxrate
# 2022-02-27T23:19:10.274343+00:00 app[web.1]: ctryprem
# 2022-02-27T23:19:10.304878+00:00 app[web.1]: histretSP
# 2022-02-27T23:19:10.305537+00:00 app[web.1]: betas
# 2022-02-27T23:19:10.331883+00:00 app[web.1]: countrytaxrates
# 2022-02-27T23:19:10.357336+00:00 app[web.1]: taxrate
# 2022-02-27T23:19:10.387063+00:00 app[web.1]: histretSP
# 2022-02-27T23:19:15.663881+00:00 app[web.1]: ref_industry_names
# 2022-02-27T23:19:15.700997+00:00 app[web.1]: ref_bonds
# 2022-02-27T23:19:16.072643+00:00 app[web.1]: ref_industry_names
# 2022-02-27T23:19:16.121705+00:00 app[web.1]: ref_bonds

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

    risk_query = db.query(
        models.table_ctryprem.country,
        models.table_ctryprem.moodys_rating,
        models.table_ctryprem.country_risk_premium,
        models.table_ctryprem.equity_risk_premium,
        models.table_ctryprem.adj_default_spread,
        )#.all()
    risk_premium_filter = risk_query.filter(func.lower(models.table_ctryprem.country).contains(func.lower(country_name))).all()
    
    if not risk_premium_filter:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    chosen_countries_l = [country[0].replace(' ','').lower() for country in risk_premium_filter]

    risk_premium = pd.DataFrame(risk_query.all())
    risk_premium['Country'] = risk_premium['country'].str.lower().str.replace(' ','')
    
    bond_query = db.query(models.table_ref_bonds.country.label('Country'),models.table_ref_bonds.yield_converted)
    bond = pd.DataFrame(bond_query.all())

    df_risk_free_all = pd.merge(risk_premium,bond,on='Country',how='left')
    df_risk_free_all['free-rate'] = df_risk_free_all['yield_converted'] - df_risk_free_all['adj_default_spread']
    df_risk_free_group_ratings = df_risk_free_all.groupby(['moodys_rating'])['free-rate'].mean().to_dict()  #.reset_index()
    df_risk_free_group_yield = df_risk_free_all.groupby(['moodys_rating'])['free-rate'].mean().to_dict()  #.reset_index()
    df_risk_free = df_risk_free_all[df_risk_free_all['Country'].isin(chosen_countries_l)]

    calculated_data = []
    for country in chosen_countries_l:
        #mask = df_risk_free[df_risk_free['Country']==country].any()
        #print(mask)
        rating = df_risk_free[df_risk_free['Country']==country]['moodys_rating'].values[0]
        yield_converted = df_risk_free[df_risk_free['Country']==country]['yield_converted'].values[0]
        risk_free = df_risk_free[df_risk_free['Country']==country]['free-rate'].values[0]
        #print(yield_converted,risk_free,rating)
        if  np.isnan(risk_free):
            risk_free = df_risk_free_group_ratings[rating]
            yield_converted = df_risk_free_group_yield[rating]
            
        calculated_data.append({'country':country,'bond_yield':yield_converted,'risk_free_rate':risk_free})

    

    return {"original_data":risk_premium_filter,"calculated_data":calculated_data}
    

# @router.get("/risk_premiums/",summary="Find risk premium for the country your firm operates in")
# async def get_risk_premium(country_name : Optional[str] = "",db:Session = Depends(get_db)):

#     if country_name.isdigit():
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail='Expecting string value.')

#     risk_premium = db.query(
#         models.table_ctryprem.country,
#         models.table_ctryprem.moodys_rating,
#         models.table_ctryprem.country_risk_premium,
#         models.table_ctryprem.equity_risk_premium,
#         models.table_ctryprem.adj_default_spread,
#         ).filter(func.lower(models.table_ctryprem.country).contains(func.lower(country_name))).all()
    
#     if not risk_premium:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
#     bond = db.query(
#         models.table_ref_bonds.country,
#         models.table_ref_bonds.yield_converted
#         ).filter(func.lower(models.table_ref_bonds.country).contains(func.lower(country_name.strip()))).all()

#     bond_dict = dict(bond)
#     risk_dict = {x[0]:x[1:] for x in risk_premium}
#     calculated_data = []
#     for key in risk_dict:
#         country_name_lowercase = (key.strip().lower().replace(' ',''))
#         try:
#             yield_converted = bond_dict[country_name_lowercase]
#         except KeyError as k:
#             yield_converted = 0
#             country_rating = (risk_dict[key][1])
#             #print(pd.DataFrame(risk_premium))
#             bond = db.query(
#                     models.table_ref_bonds.country,
#                     func.mean(models.table_ref_bonds.yield_converted),
#                         ).groupby()
#             #print(pd.read_sql((risk_premium)))
#             print('It failed bacause we dont have a bond rate for that country.')
#             print('This needs to be fixed in future versions.')

#         risk_free = np.abs(yield_converted - risk_dict[key][3])
#         calculated_data.append({'country':key,'bond_yield':yield_converted,'risk_free_rate':risk_free})
    

#     return {"original_data":risk_premium,"calculated_data":calculated_data}