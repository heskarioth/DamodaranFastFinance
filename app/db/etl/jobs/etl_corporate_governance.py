import pandas as pd
from ....config import etl_settings
import numpy as np
import pandas as pd
from datetime import datetime
def f_inhold():
    # extract
    df = pd.read_html(etl_settings.inshold,header=[0])[0]
    # validate input - first we expect certain column names in this order here.
    validation_list = ['Industry  Name', 'Number of Firms', 'CEO Holding','Institutional Holdings', 'Insider Holdings']
    if sum(df.columns == validation_list)==len(validation_list):
        #transform
        #convert columns to floats, remove percentage symbol
        for col in df[['CEO Holding','Institutional Holdings', 'Insider Holdings']].columns:
            df[col]=df[col].str.replace('%','',regex=True).astype(np.float64) / 100
        #match column names to table name
        df['created_at'] = datetime.now()
        df.fillna(0,inplace=True)
        df.columns=["industry_name","number_of_firms","ceo_holding","institutional_holdings","insider_holdings","created_at"]
        return df
    else:
        return ('Error')
        #raise ValueTooSmallError
