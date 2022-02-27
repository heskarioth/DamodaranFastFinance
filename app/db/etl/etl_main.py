import sys,os
from sqlalchemy.orm import Session
from .. import database, models
from ...config import etl_settings
import numpy as np
import pandas as pd
from datetime import datetime, timezone, timedelta
from ..etl.jobs import etl_corporate_governance as cg
from ..etl.jobs import etl_cashflow_estimation as cfe
from ..etl.jobs import etl_discount_rate as dr
from ..etl.jobs import etl_growth_rate_estimation as gre
from ..etl.jobs import etl_dividend_policy as dp
from ..etl.jobs import etl_capital_structure as cs
from ..etl.jobs import etl_reference_items as ref_items

from ...config import etl_settings
var =2 
# open session
db = database.SessionLocal()
#check if new files have been uploaded



feeds_reference = {
    'fundgrEB' : {'function':gre.f_fundgrEB(),'table':models.table_fundgrEB,'datefeed_url':etl_settings.fundgrEB}
    ,'histgr' : {'function':gre.f_histgr(),'table':models.table_histgr,'datefeed_url':etl_settings.histgr}
    ,'roe' : {'function':gre.f_roe(),'table':models.table_roe,'datefeed_url':etl_settings.roe}
    ,'fundgr' : {'function':gre.f_fundgr(),'table':models.table_fundgr,'datefeed_url':etl_settings.fundgr}
    ,'inhold' : {'function':cg.f_inhold(),'table':models.table_inhold,'datefeed_url':etl_settings.inhold}
    ,'wcdata' : {'function':cfe.f_wcdata(),'table':models.table_wcdata,'datefeed_url':etl_settings.wcdata}
    ,'finflows' : {'function':cfe.f_finflows(),'table':models.table_finflows,'datefeed_url':etl_settings.finflows}
    ,'histimpl' : {'function':dr.f_histimpl(),'table':models.table_histimpl,'datefeed_url':etl_settings.histimpl}
    ,'margin' : {'function':cfe.f_margin(),'table':models.table_margin,'datefeed_url':etl_settings.margin}
    ,'goodwill' : {'function':cfe.f_goodwill(),'table':models.table_goodwill,'datefeed_url':etl_settings.goodwill}
    ,'r_d' : {'function':cfe.f_r_d(),'table':models.table_r_d,'datefeed_url':etl_settings.r_d}
    ,'capex' : {'function':cfe.f_capex(),'table':models.table_capex,'datefeed_url':etl_settings.capex}
    ,'divfcfe' : {'function':dp.f_divfcfe(),'table':models.table_divfcfe,'datefeed_url':etl_settings.divfcfe}
    ,'macro' : {'function':cs.f_macro(),'table':models.table_macro,'datefeed_url':etl_settings.macro}
    ,'dbtfund' : {'function':cs.f_dbtfund(),'table':models.table_dbtfund,'datefeed_url':etl_settings.dbtfund}
    ,'debtdetails' : {'function':cs.f_debtdetails(),'table':models.table_debtdetails,'datefeed_url':etl_settings.debtdetails}
    ,'leaseeffect' : {'function':cs.f_leaseeffect(),'table':models.table_leaseeffect,'datefeed_url':etl_settings.leaseeffect}
    ,'wacc' : {'function':dr.f_wacc(),'table':models.table_wacc,'datefeed_url':etl_settings.wacc}
    ,'totalbeta' : {'function':dr.f_totalbeta(),'table':models.table_totalbeta,'datefeed_url':etl_settings.totalbeta}
    ,'ctryprem' : {'function':dr.f_ctryprem(),'table':models.table_ctryprem,'datefeed_url':etl_settings.ctryprem}
    ,'betas' : {'function':dr.f_betas(),'table':models.table_betas,'datefeed_url':etl_settings.betas}
    ,'countrytaxrates' : {'function':dr.f_countrytaxrates(),'table':models.table_countrytaxrates,'datefeed_url':etl_settings.countrytaxrates}
    ,'taxrate' : {'function':dr.f_taxrate(),'table':models.table_taxrate,'datefeed_url':etl_settings.taxrate}
    ,'histretSP' : {'function':dr.f_histretSP(),'table':models.table_histretSP,'datefeed_url':etl_settings.histretSP}
    ,'ref_industry_names' : {'function':ref_items.f_ref_industry_names(),'table':models.table_ref_industry_names,'datefeed_url':etl_settings.ref_industry_names}
    ,'ref_bonds' : {'function':ref_items.f_ref_bond(),'table':models.table_ref_bonds,'datefeed_url':etl_settings.ref_industry_names}
    }



    


def scheduler_updater(feed):
    df = feeds_reference[feed]['function'].to_dict(orient='records')
    db.query(feeds_reference[feed]['table']).delete()
    db.commit()
    schedule_update = models.table_backend_refresh_schedules(**{'datafeed_name':feed,'lastupdate_at':datetime.now(),'datefeed_url':etl_settings.__dict__[feed]})
    db.add(schedule_update)
    db.bulk_insert_mappings(feeds_reference[feed]['table'], df)
    db.commit()
    print(feed)

def scheduler_orchestrator(feed):
    match feed:
        case 'fundgrEB':
            scheduler_updater(feed)
        case 'histgr':
            scheduler_updater(feed)
        case 'roe':
            scheduler_updater(feed)
        case 'fundgr':
            scheduler_updater(feed)
        case 'inhold':
            scheduler_updater(feed)
        case 'wcdata':
            scheduler_updater(feed)
        case 'finflows':
            scheduler_updater(feed)
        case 'histimpl': 
            scheduler_updater(feed)
        case 'margin':
            scheduler_updater(feed)
        case 'goodwill':
            scheduler_updater(feed)
        case 'r_d': 
            scheduler_updater(feed)
        case 'capex':
            scheduler_updater(feed)
        case 'divfcfe':
            scheduler_updater(feed)
        case 'macro':
            scheduler_updater(feed)
        case 'dbtfund':
            scheduler_updater(feed)
        case 'debtdetails':
            scheduler_updater(feed)
        case 'leaseeffect':
            scheduler_updater(feed)
        case 'wacc':
            scheduler_updater(feed)
        case 'totalbeta':
            scheduler_updater(feed)
        case 'ctryprem':
            scheduler_updater(feed)
        case 'betas':
            scheduler_updater(feed)
        case 'countrytaxrates':
            scheduler_updater(feed)
        case 'taxrate':
            scheduler_updater(feed) 
        case 'histretSP':
            scheduler_updater(feed)
        case 'ref_industry_names':
            scheduler_updater(feed)
        case 'ref_bonds':
            scheduler_updater(feed)
        case _:
            return "No updates required."


# ping once a day
#last_update = Feb 2022
#check last update
    #if month now - month last update >0:
        # update all data
        # update last_update
#check if there are no entries, if no entries, update all.


# Check if there are tables added to db. If not run all and add.
is_data = db.query(models.table_backend_refresh_schedules).all()
if len(is_data)<1:
    for feed in feeds_reference:
        scheduler_orchestrator(feed)
else:
    # We have some tables already. Now we check if the ones we have need update (more than 30 days old)
    # Or if we included new tables that needs to be added to the list
    schedules = db.query(models.table_backend_refresh_schedules).all() # extract current record and turn it into a df.
    df_schedules = pd.DataFrame()
    for schedule in schedules:
        df_schedules = pd.concat([df_schedules,pd.DataFrame({'datafeed_name':schedule.datafeed_name,'lastupdate_at':schedule.lastupdate_at,'datefeed_url':schedule.datefeed_url},index=[0])])
    df_schedules = df_schedules.groupby(['datafeed_name'])['lastupdate_at'].max()
    
    feeds_to_add = [] # new tables to be added
    feeds_to_update = [] #old tables that need to be updated
    for schedule in df_schedules.reset_index().to_dict(orient='records'):
        #schedule['lastupdate_at']= schedule['lastupdate_at'].astimezone(timezone.utc) + timedelta(days=60) # for testing
        # if older than 1 month, add them to list for updating
        if(np.abs(datetime.now(timezone.utc) - schedule['lastupdate_at'].astimezone(timezone.utc)).days/ 30)>0.90:
            feeds_to_update.append(schedule['datafeed_name'])
    
    #add new tables
    for feed in feeds_reference:
        if feed not in df_schedules.index:
            feeds_to_add.append(feed)
    for feed in feeds_to_add:
        scheduler_orchestrator(feed)
    #update old tables
    for feed in feeds_to_update:
        scheduler_orchestrator(feed)





    
