import pandas as pd
from ....config import etl_settings
import numpy as np
import pandas as pd
from datetime import datetime

def percentage_remover_with_div_0(x):
    if isinstance(x,float):
        return x
    if isinstance(x,int):
        return x
    if '#VALUE' in x:
        return 0
    return np.float64(x.replace('%','').replace('#DIV/0!','0'))/ 100
    
def parenthesis_number_zero_minus(x):
        # $ 6,932
        # $ (21,328)
        # $  -  
        # $ 0
        # ####
    if isinstance(x,float):
        return x
    if isinstance(x,int):
        return x
    if '$' in x:
        x = x.replace('$','').replace(' ','').replace(',','')
    if '-' in x and len(x)==1:
            return np.float64(x.replace('-','').replace('','0'))
    if '#' in x:
        return 0
    if '-' in x:
        return np.float(x)
    if '(' in x:
        return -1 * np.float64(x.replace('$','').replace(' ','').replace('(','').replace(')','').replace(',',''))
    else:
        return np.float64(x.replace('$','').replace(' ','').replace('(','').replace(')','').replace(',',''))


def f_eva(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.histretSP,header=1)[0]
    validation_list = ['Industry  Name', 'Number of Firms', 'Beta', 'ROE', 'Cost of Equity','(ROE - COE)', 'BV of Equity', 'Equity EVA (US $ millions)', 'ROC','Cost of Capital', '(ROC - WACC)', 'BV of Capital','EVA (US $ millions)']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['ROE', 'Cost of Equity','(ROE - COE)','ROC','Cost of Capital', '(ROC - WACC)']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        for col in ['BV of Equity', 'Equity EVA (US $ millions)', 'BV of Capital','EVA (US $ millions)']:
            df[col] = df[col].apply(parenthesis_number_zero_minus)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'beta', 'roe_pct', 'cost_of_equity_coe_pct','roe_minus_coe_pct', 'bv_of_equity_usd', 'equity_eva_in_mil_usd', 'roc_pct','cost_of_capital_pct', 'roc_minus_wacc_pct', 'bv_of_capital_usd','eva_in_mil_usd','created_at']
        return df
    else:
        return 'Error'