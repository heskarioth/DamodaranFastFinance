import pandas as pd
from ....config import etl_settings
import numpy as np
import pandas as pd
from datetime import datetime
import numpy as np


def f_ref_industry_names():
    df = pd.read_excel(etl_settings.ref_industry_names)
    df.dropna(subset=['Exchange:Ticker'],inplace=True)
    df['ticker'] = df['Exchange:Ticker'].str.split(':').str[1].str.upper()
    df['created_at'] = datetime.now()
    df.columns = ['company_name', 'exchange_ticker', 'industry_group', 'primary_sector','sic_code', 'country', 'broad_group', 'sub_group','ticker','created_at']
    return df

def f_ref_bond():
    
    #getting bond rates from first datasource
    url = 'https://tradingeconomics.com/bonds'
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