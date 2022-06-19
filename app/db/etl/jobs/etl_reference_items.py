import functools
import pandas as pd
from ....config import etl_settings
import numpy as np
import pandas as pd
from datetime import datetime
import numpy as np
import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import List
from pandas import DataFrame
import re

def f_ref_industry_names(data):

    def transform(x):
        return re.sub(r'[^\w]','',x.replace(' ','').upper())


    batch_size = 2000
    urls : List = [f'ref_industry_name/industry_data_{start}.csv' for start in range(0,47606,batch_size)]
    df_lists : List = [pd.read_csv(url) for url in urls]
    df = pd.concat(df_lists)

    df.dropna(subset=['Exchange:Ticker'],inplace=True)
    df['ticker'] = df['Exchange:Ticker'].str.split(':').str[1].str.upper()
    df['industry_group_fk'] = df['Industry Group'].apply(transform)
    df['created_at'] = datetime.now()
    df.columns = ['company_name', 'exchange_ticker', 'industry_group', 'primary_sector','sic_code', 'country', 'broad_group', 'sub_group','ticker','industry_group_fk','created_at']
    return df


def f_ref_industry_names_bk(data):
    """Online function to get the data."""
    def send_request(url: str) -> DataFrame:
        return pd.read_html(url)[0]

    async def f_ref_industry_names_async() -> DataFrame:
        batch_size = 2000
        loop = asyncio.get_running_loop()
        urls : List = [f'https://github.com/heskarioth/DamodaranFastFinance/blob/master/ref_industry_name/industry_data_{start}.csv' for start in range(0,47606,batch_size)]
        with ThreadPoolExecutor() as pool:
            tasks = [loop.run_in_executor(pool,functools.partial(send_request,url)) for url in urls]
            df_lists = []
            for finished_task in asyncio.as_completed(tasks):
                df_lists.append(await finished_task)
            
        return pd.concat(df_lists)

    df = asyncio.run(f_ref_industry_names_async())
    df.dropna(subset=['Exchange:Ticker'],inplace=True)
    df['ticker'] = df['Exchange:Ticker'].str.split(':').str[1].str.upper()
    df['created_at'] = datetime.now()
    df.columns = ['company_name', 'exchange_ticker', 'industry_group', 'primary_sector','sic_code', 'country', 'broad_group', 'sub_group','ticker','created_at']
    return df

def f_ref_bond(data):
    #getting bond rates from first datasource
    url = 'http://tradingeconomics.com/bonds'
    bonds_tradingeconomics = pd.read_html(url)[0][['Major10Y', 'Yield']]
    bonds_tradingeconomics.columns = ['Country','Yield']
    bonds_tradingeconomics['Country'] = bonds_tradingeconomics['Country'].str.replace('\W','',regex=True).str.lower()
    bonds_tradingeconomics['Yield_converted'] = bonds_tradingeconomics['Yield'].astype(np.float64)/100
    
    #getting bond rates from second datasource
    url = 'http://www.worldgovernmentbonds.com/'
    bonds_worldgovernmentbonds = pd.read_html(url)[0][['Country','10Y Yield']]
    bonds_worldgovernmentbonds.columns = ['Country','Yield']
    bonds_worldgovernmentbonds['Yield_converted'] = bonds_worldgovernmentbonds['Yield'].str.replace('%','').astype(np.float64)/100
    bonds_worldgovernmentbonds['Country'] = bonds_worldgovernmentbonds['Country'].str.replace('\W','',regex=True).str.lower()
    
    df = pd.concat([bonds_tradingeconomics,bonds_worldgovernmentbonds]).groupby('Country')['Yield_converted'].mean().reset_index()
    
    df['created_at'] = datetime.now()
    df.columns = ['country', 'yield_converted', 'created_at']
    
    return df