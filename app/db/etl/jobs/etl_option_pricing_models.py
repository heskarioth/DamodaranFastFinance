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
    return np.float64(x.replace('%','').replace('#DIV/0!','0'))/ 100
    

def f_optvar(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.histretSP,header=1)[0]
    validation_list = ['Industry  Name', 'Number of Firms', 'Std Deviation in Equity','Std Deviation in Firm Value', 'E/(D+E)', 'D/(D+E)']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Std Deviation in Equity','Std Deviation in Firm Value', 'E/(D+E)', 'D/(D+E)']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'std_dev_equity_pct','std_dev_firm_value_pct', 'equity_divided_by_debt_plus_equity_pct', 'debt_divided_bt_debt_plus_equity_pct','created_at']
        return df
    else:
        return 'Error'