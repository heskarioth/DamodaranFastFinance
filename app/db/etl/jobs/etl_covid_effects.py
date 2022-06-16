import pandas as pd
from ....config import etl_settings
import numpy as np
import pandas as pd
from datetime import datetime


def parenthesis_number_zero_minus(x):
        # $ 6,932
        # $ (21,328)
        # $  -  
        # $ 0
    if isinstance(x,float):
        return x
    if isinstance(x,int):
        return x
    if '$' in x:
        x = x.replace('$','').replace(' ','').replace(',','')
    if '-' in x and len(x)==1:
            return np.float64(x.replace('-','').replace('','0'))
    if '-' in x:
        return np.float(x)
    if '(' in x:
        return -1 * np.float64(x.replace('$','').replace(' ','').replace('(','').replace(')','').replace(',',''))
    else:
        return np.float64(x.replace('$','').replace(' ','').replace('(','').replace(')','').replace(',',''))

def percentage_remover_with_div_0(x):
    if isinstance(x,float):
        return x
    if isinstance(x,int):
        return x
    return np.float64(x.replace('%','').replace('#DIV/0!','0'))/ 100

def dollar_adjuster_minus_head(x):
    #example input string: -$457.54
    if isinstance(x,float):
        return x
    return np.float64(x.replace(',','').replace('$',''))


def f_covideffects(data):
    df = pd.read_html(data,header=1)[0]
    #df = pd.read_html(etl_settings.histretSP,header=1)[0]
    validation_list = ['Industry  Name', 'Number  of firms', '12/31/19', '2/14/20', '3/20/20','9/1/20', '12/31/21', '1/1/20  - 2/14', '2/14/20  - 3/20/20','3/20/20  - 9/1/20', '9/1/20  - 12/31/21', '1/1/20  - 12/31/21','LTM  2020', 'LTM  2021', '%  Change', 'LTM  20202', 'LTM  20213','%  Change4']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['1/1/20  - 2/14','2/14/20  - 3/20/20','3/20/20  - 9/1/20','9/1/20  - 12/31/21','1/1/20  - 12/31/21','%  Change4','%  Change']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        for col in ['12/31/19','2/14/20','3/20/20','9/1/20','LTM  2020','LTM  2021']:
            df[col] = df[col].apply(dollar_adjuster_minus_head)
        for col in 'LTM  20202','LTM  20213':
            df[col] = df[col].apply(parenthesis_number_zero_minus)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'markcap_12_31_19_usd', 'markcap_2_14_20_usd', 'markcap_3_20_20_usd','markcap_9_1_20_usd', 'markcap_12_31_21_usd', 'pct_chg_1_1_20_to_2_14_20', 'pct_chg_2_14_20_to_3_20_20','pct_chg_3_20_20_to_9_1_20', 'pct_chg_9_1_20_to_12_31_21', 'pct_chg_1_1_20_to_12_31_21','revenues_ltm_2020', 'revenues_ltm_2021', 'revenues_pct_chg', 'op_income_ltm_20202', 'op_income_ltm_20213','op_income_pct_chg','created_at']
        return df
    else:
        return 'Error'