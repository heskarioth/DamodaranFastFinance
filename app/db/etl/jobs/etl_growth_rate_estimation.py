import pandas as pd
from ....config import etl_settings
import numpy as np
import pandas as pd
from datetime import datetime

def f_roe():
    df = pd.read_html(etl_settings.roe,header=0)[0]
    validation_list = ['Industry Name', 'Number of firms', 'ROE (unadjusted)','ROE (adjusted for R&D)']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['ROE (unadjusted)','ROE (adjusted for R&D)']:
            df[col] = df[col].str.replace('%','',regex=True).astype(np.float64)/100
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name','number_of_firms','roe_unadjusted','roe_adjusted_for_r_and_d','created_at']
        return df
    else:
        return 'Error'
    
def f_fundgr(): #yep
    df = pd.read_html(etl_settings.fundgr,header=0)[0]
    validation_list = ['Industry  Name', 'Number of Firms', 'ROE', 'Retention Ratio','Fundamental Growth']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['ROE', 'Retention Ratio','Fundamental Growth']:
            df[col] = df[col].str.replace('%','',regex=True).astype(np.float64)/100
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'roe', 'retention_rate_percentage','fundamental_growth_percentage','created_at']
        return df
    else:
        return 'Error'

## use this one
def f_histgr(): #yep
    df = pd.read_html(etl_settings.histgr,header=0)[0]
    validation_list = ['Industry  Name', 'Number of Firms','CAGR in Net Income- Last 5  years', 'CAGR in Revenues- Last 5  years','Expected  Growth in Revenues - Next 2 years','Expected  Growth in EPS - Next 5 years']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['CAGR in Net Income- Last 5  years', 'CAGR in Revenues- Last 5  years','Expected  Growth in Revenues - Next 2 years','Expected  Growth in EPS - Next 5 years']:
            df[col] = df[col].str.replace('#DIV/0!','0%',regex=True).str.replace('%','',regex=True).astype(np.float64)/100
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms','cagr_in_net_income_last_5_years_percentage', 'cagr_in_revenues_last_5_years_percentage','expected_growth_in_revenues_next_2_years_percentage','expected_growth_in_eps_next_5_years_percentage','created_at']
        return df
    else:
        return 'Error'

def f_fundgrEB(): #yep
    df = pd.read_html(etl_settings.fundgrEB,header=0)[0]
    validation_list = ['Industry  Name', 'Number of Firms', 'ROC', 'Reinvestment Rate','Expected Growth in EBIT']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['ROC', 'Reinvestment Rate','Expected Growth in EBIT']:
            df[col] = df[col].str.replace('#DIV/0!','0%',regex=True).str.replace('%','',regex=True).astype(np.float64)/100
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'roc_percentage', 'reinvestment_rate_percentage','expected_growth_in_ebit_percentage','created_at']
        return df
    else:
        return 'Error'