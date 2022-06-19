import logging
import asyncio
import aiohttp
from aiohttp import ClientSession
from sqlalchemy.orm import Session
from .. import database, models
from ... config import etl_settings
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
from ..etl.jobs import etl_dollar_value as dv
from ..etl.jobs import etl_covid_effects as ce
from ..etl.jobs import etl_multiples as mul
from ..etl.jobs import etl_option_pricing_models as opm
from ..etl.jobs import etl_return_measures as ret_m
from typing import List
from ...config import etl_settings

# ping once a day
#last_update = Feb 2022
#check last update
    #if month now - month last update >0:
        # update all data
        # update last_update
#check if there are no entries, if no entries, update all.

db = database.SessionLocal()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

feeds_reference = {
    'fundgrEB' : {'function':gre.f_fundgrEB,'table':models.table_fundgrEB,'datefeed_url':etl_settings.fundgrEB}
    ,'histgr' : {'function':gre.f_histgr,'table':models.table_histgr,'datefeed_url':etl_settings.histgr}
    ,'roe' : {'function':gre.f_roe,'table':models.table_roe,'datefeed_url':etl_settings.roe}
    ,'fundgr' : {'function':gre.f_fundgr,'table':models.table_fundgr,'datefeed_url':etl_settings.fundgr}
    ,'inhold' : {'function':cg.f_inhold,'table':models.table_inhold,'datefeed_url':etl_settings.inhold}
    ,'wcdata' : {'function':cfe.f_wcdata,'table':models.table_wcdata,'datefeed_url':etl_settings.wcdata}
    ,'finflows' : {'function':cfe.f_finflows,'table':models.table_finflows,'datefeed_url':etl_settings.finflows}
    ,'histimpl' : {'function':dr.f_histimpl,'table':models.table_histimpl,'datefeed_url':etl_settings.histimpl}
    ,'margin' : {'function':cfe.f_margin,'table':models.table_margin,'datefeed_url':etl_settings.margin}
    ,'goodwill' : {'function':cfe.f_goodwill,'table':models.table_goodwill,'datefeed_url':etl_settings.goodwill}
    ,'r_d' : {'function':cfe.f_r_d,'table':models.table_r_d,'datefeed_url':etl_settings.r_d}
    ,'capex' : {'function':cfe.f_capex,'table':models.table_capex,'datefeed_url':etl_settings.capex}
    ,'divfcfe' : {'function':dp.f_divfcfe,'table':models.table_divfcfe,'datefeed_url':etl_settings.divfcfe}
    ,'macro' : {'function':cs.f_macro,'table':models.table_macro,'datefeed_url':etl_settings.macro}
    ,'dbtfund' : {'function':cs.f_dbtfund,'table':models.table_dbtfund,'datefeed_url':etl_settings.dbtfund}
    ,'debtdetails' : {'function':cs.f_debtdetails,'table':models.table_debtdetails,'datefeed_url':etl_settings.debtdetails}
    ,'leaseeffect' : {'function':cs.f_leaseeffect,'table':models.table_leaseeffect,'datefeed_url':etl_settings.leaseeffect}
    ,'wacc' : {'function':dr.f_wacc,'table':models.table_wacc,'datefeed_url':etl_settings.wacc}
    ,'totalbeta' : {'function':dr.f_totalbeta,'table':models.table_totalbeta,'datefeed_url':etl_settings.totalbeta}
    ,'ctryprem' : {'function':dr.f_ctryprem,'table':models.table_ctryprem,'datefeed_url':etl_settings.ctryprem}
    ,'betas' : {'function':dr.f_betas,'table':models.table_betas,'datefeed_url':etl_settings.betas}
    ,'countrytaxrates' : {'function':dr.f_countrytaxrates,'table':models.table_countrytaxrates,'datefeed_url':etl_settings.countrytaxrates}
    ,'taxrate' : {'function':dr.f_taxrate,'table':models.table_taxrate,'datefeed_url':etl_settings.taxrate}
    ,'histretSP' : {'function':dr.f_histretSP,'table':models.table_histretSP,'datefeed_url':etl_settings.histretSP}
    ,'dollarus' : {'function':dv.f_dollarus,'table':models.table_dollarus,'datefeed_url':etl_settings.dollarus}
    ,'covideffects' : {'function':ce.f_covideffects,'table':models.table_covideffects,'datefeed_url':etl_settings.covideffects}
    ,'pedata' : {'function':mul.f_pedata,'table':models.table_pedata,'datefeed_url':etl_settings.pedata}
    ,'pbvdata' : {'function':mul.f_pbvdata,'table':models.table_pbvdata,'datefeed_url':etl_settings.pbvdata}
    ,'psdata' : {'function':mul.f_psdata,'table':models.table_psdata,'datefeed_url':etl_settings.psdata}
    ,'countrystats' : {'function':mul.f_countrystats,'table':models.table_countrystats,'datefeed_url':etl_settings.countrystats}
    ,'optvar' : {'function':opm.f_optvar,'table':models.table_optvar,'datefeed_url':etl_settings.optvar}
    ,'eva' : {'function':ret_m.f_eva,'table':models.table_eva,'datefeed_url':etl_settings.eva}
    ,'vebitda' : {'function':mul.f_vebitda,'table':models.table_vebitda,'datefeed_url':etl_settings.vebitda}    
    ,'mktcaprisk' : {'function':dr.f_mktcaprisk,'table':models.table_mktcaprisk,'datefeed_url':etl_settings.mktcaprisk}
    
    ,'mktcapmult' : {'function':mul.f_mktcapmult,'table':models.table_mktcapmult,'datefeed_url':etl_settings.mktcapmult}

    #,'ref_industry_names' : {'function':ref_items.f_ref_industry_names,'table':models.table_ref_industry_names,'datefeed_url':etl_settings.ref_industry_names} - we don't want to update this to db.
    # ,'ref_bonds' : {'function':ref_items.f_ref_bond,'table':models.table_ref_bonds,'datefeed_url':etl_settings.ref_industry_names} --> needs to be fixed
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

async def send_request(session : ClientSession, **kwargs : dict) -> str:
    async with session.request(kwargs['method'],kwargs['url'], params=kwargs['params']) as result:
        if result.status!=200:
            print('Failed getting page.')
            failed_executions.append(kwargs)
            raise aiohttp.ClientError()
        else:
            good_executions.append({'data':await result.read(),'feed_name':kwargs['feed_name']})
        return result


async def search_feed(payloads_exc_commands) -> List:
    global failed_executions, good_executions
    failed_executions = []
    good_executions = []
    batch_size = 20
    for start in range(0,len(payloads_exc_commands),batch_size):
        async with ClientSession() as session:
            pending = [asyncio.create_task(send_request(session,**payload)) for payload in payloads_exc_commands[start:start+batch_size]]

            while pending:
                
                done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_EXCEPTION)

                for done_task in done:
                    if done_task.exception():
                        new_tasks = [
                            asyncio.create_task(send_request(session,payload)) for payload in failed_executions
                        ]
                        failed_executions = []

                        for new_task in new_tasks:
                            pending.add(new_task)
    return good_executions


def datafeed_updater(df : pd.DataFrame,feed_name : str) -> None:
    df = df.to_dict(orient='records')
    db.query(feeds_reference[feed_name]['table']).delete() # we are removing old months data.
    db.commit()
    schedule_update = models.table_backend_refresh_schedules(**{'datafeed_name':feed_name,'lastupdate_at':datetime.now(),'datefeed_url':etl_settings.__dict__[feed_name]})
    db.add(schedule_update)
    db.bulk_insert_mappings(feeds_reference[feed_name]['table'], df)
    db.commit()


import time
import numpy as np
def main_etl() -> None:
    feeds_in_db = [row.datafeed_name for row in db.query(models.table_backend_refresh_schedules).all()]
    print(f'Feeds in db: {feeds_in_db} ({len(feeds_in_db)})')
    
    # Check if there are tables that are missing from database.
    feeds_to_add = [] #keep track of new tables here.
    for feed in feeds_reference.keys():
        if feed not in feeds_in_db:
            feeds_to_add.append(feed)

    # Check of the existing tables if they have been refreshed in the last month
    df_schedules = pd.DataFrame()
    for schedule in db.query(models.table_backend_refresh_schedules).all():
        df_schedules = pd.concat([df_schedules,pd.DataFrame({'datafeed_name':schedule.datafeed_name,'lastupdate_at':schedule.lastupdate_at,'datefeed_url':schedule.datefeed_url},index=[0])])
    df_schedules = df_schedules.groupby(['datafeed_name'])['lastupdate_at'].max()
    feeds_to_update = [] #keep track of old tables that need to be updated here.
    for schedule in df_schedules.reset_index().to_dict(orient='records'):
        #schedule['lastupdate_at']= schedule['lastupdate_at'].astimezone(timezone.utc) + timedelta(days=60) # for testing
        # if last update older than 1 month, add them to list for updating
        if(np.abs(datetime.now(timezone.utc) - schedule['lastupdate_at'].astimezone(timezone.utc)).days/ 30)>0.90:
            feeds_to_update.append(schedule['datafeed_name'])
    
    # merge list feeds and begin search.
    feed_executions = list(set(feeds_to_add + feeds_to_update))
    print(f'Feeds that need to be added/updated in db: {feed_executions} ({len(feed_executions)})')
    if len(feed_executions)>0:
        payloads_exc_commands = [{
            'method':'GET'
            ,'url': feeds_reference[feed_name]['datefeed_url']
            ,'params':''
            ,'feed_name':feed_name
            } for feed_name in feed_executions]
        
        results = asyncio.run(search_feed(payloads_exc_commands))
        times = []
        for result in results:
            # parse data response to dataframe
            feed_name = result['feed_name']
            start = time.time() # this takes a threadingExcutor
            df = feeds_reference[feed_name]['function'](result['data'])
            end = time.time()
            # upload data to db
            print(feed_name)
            datafeed_updater(df,feed_name)
            times.append(end-start)
        
        print(f'Mean time taken: {np.mean(times)}')
        print(f'Total time taken: {np.sum(times)}')
        print(f'Times: {times}')
    else:
        print('No table requires update.')
        



main_etl()




# how to run the module: py -m app.db.etl.etl_main
# location: (damo) PS C:\Users\camil\OneDrive\Desktop\My Projects\FastAPIDamo> 
# - replace referencetable - with a readfile from git. do look up there DONE
# - rewrite the data collection script to be async. DONE
# - rewrite the data insertion part ot be async as well. - NOT NECESSARY
# - create a monitoring framework to check data has not changed. 
# - continue adding the remaning pipelines. - DONE.
# - add docstrings
