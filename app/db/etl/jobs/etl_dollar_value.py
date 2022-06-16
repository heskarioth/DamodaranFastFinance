import pandas as pd
from ....config import etl_settings
import numpy as np
import pandas as pd
from datetime import datetime


def paranthesis_number(x):
    # This is the right one to keep

    #example input $                                           (200.96) => - 200.96
    if isinstance(x,float):
        return x
    if isinstance(x,int):
        return x
    if '(' in x:
        return -1 * np.float64(x.replace('$','').replace(' ','').replace('(','').replace(')','').replace(',',''))
    else:
        return np.float64(x.replace('$','').replace(' ','').replace('(','').replace(')','').replace(',',''))



def f_dollarus(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.histretSP,header=1)[0]
    validation_list = ['Industry Name', 'Number of firms', 'Market Cap ($ millions)','Book Equity ($ millions)', 'Enteprise Value ($ millions)','Invested Capital ($ millions)','Total Debt (including leases) ($ millions)', 'Revenues ($ millions)','Gross Profit ($ millions)', 'EBITDA ($ millions)','EBIT (Operating Income) ($ millions)', 'Net Income ( $ millions)']
    if sum(df.columns==validation_list)==len(validation_list):
#         for col in ['Cash/Firm  Value','Market  Debt to capital ratio (median)','Standard deviation in stock price (median)']:
#             df[col] = df[col].apply(percentage_remover_with_div_0)
        for col in ['Market Cap ($ millions)','Book Equity ($ millions)', 'Enteprise Value ($ millions)','Invested Capital ($ millions)','Total Debt (including leases) ($ millions)', 'Revenues ($ millions)','Gross Profit ($ millions)', 'EBITDA ($ millions)','EBIT (Operating Income) ($ millions)', 'Net Income ( $ millions)']:
            df[col] = df[col].apply(paranthesis_number)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'markcap_in_mil_usd','book_equity_in_mil_usd','enteprise_value_in_mil_usd','invested_capital_in_mil_usd','total_debt_including_leases_in_mil_usd', 'revenues_in_mil_usd','gross_profit_in_mil_usd', 'ebitda_in_mil_usd','ebit_op_income_in_mil_usd', 'net_income_in_mil_usd','created_at']
        return df
    else:
        return 'Error'
    