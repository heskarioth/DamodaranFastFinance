import pandas as pd
from ....config import etl_settings
import numpy as np
import pandas as pd
from datetime import datetime

# transformation functions

def percentage_remover(x):
    if isinstance(x,float):
        return x
    return np.float64(x.replace('%',''))/ 100

def percentage_remover_with_div_0(x):
    if isinstance(x,float):
        return x
    return np.float64(x.replace('%','').replace('#DIV/0!','0'))/ 100

def dollar_adjuster_minus_head(x):
    #example input string: -$457.54
    if isinstance(x,float):
        return x
    return np.float64(x.replace(',','').replace('$',''))

def dollar_adjuster_minus_blank(x):
    #example input string: -$  -  
    if isinstance(x,float):
        return x
    return np.float64(x.replace(',','').replace('$','').replace('-','0'))



def f_divfcfe(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.divfcfe,header=0)[0]
    validation_list = ['Industry  name', 'Number of firms', 'Dividends', 'Net Income','Payout', 'Dividends + Buybacks', 'Cash Return as % of Net  Income','Dividends + Buybacks - Stock  Issuances','FCFE (before debt cash  flows)', 'FCFE (after debt cash flows)','Net Cash Returned/FCFE  (pre-debt)','Net Cash Returned/FCFE  (post-debt)', 'Net Cash Returned/ Net  Income','Cash/ Firm Value']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Payout','Net Cash Returned/ Net  Income','Cash/ Firm Value','Cash Return as % of Net  Income','Net Cash Returned/FCFE  (pre-debt)','Net Cash Returned/FCFE  (post-debt)']:
            df[col] = df[col].apply(percentage_remover)
        for col in ['Dividends','Net Income','Dividends + Buybacks - Stock  Issuances','FCFE (before debt cash  flows)', 'FCFE (after debt cash flows)']:
            df[col] = df[col].apply(dollar_adjuster_minus_head)
        for col in ['Dividends + Buybacks','FCFE (before debt cash  flows)']:
            df[col] = df[col].apply(dollar_adjuster_minus_blank)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'dividends', 'net_income_usd','payout_in_percentage', 'dividends_plus_buybacks_usd', 'cash_returns_as_percentage_of_net_income','dividends_plus_buybacks_minus_stock_issuances_usd','fcfe_before_debt_cash_flows_usd', 'fcfe_after_debt_cash_flows_usd','net_cash_returned_fcfe_pre_debt_percentage','net_cash_returned_fcfe_post_debt_percentage', 'net_cash_returned_divided_by_fcfe_post_debt_percentage','cash_divided_by_frim_value_percentage', 'created_at']
        return df
    else:
        return 'Error'

def f_divfund():
    df = pd.read_html(etl_settings.divfund,header=0)[0]
    validation_list = ['Industry Name', 'Number of firms', 'Total Dividends (US $ millions)','Special Dividends as % of Total Dividends', 'Dividend Payout','Dividend Yield', 'Market Cap (US $ millions)', 'ROE','Institutional Holdings', 'Std Dev in Stock Prices']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Special Dividends as % of Total Dividends', 'Dividend Payout','Dividend Yield','ROE','Institutional Holdings', 'Std Dev in Stock Prices']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        for col in ['Total Dividends (US $ millions)', 'Market Cap (US $ millions)']:
            df[col] = df[col].apply(dollar_adjuster_minus_blank)
#         for col in ['Dividends + Buybacks','FCFE (before debt cash  flows)']:
#             df[col] = df[col].apply(dollar_adjuster_minus_blank)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'total_dividends_usd_millions','special_dividends_as_percentage_of_total_dividends', 'dividend_payout_percentage','dividend_yield_percentage', 'market_cap_usd_millions', 'roe_percentage','institutional_holdings_percentage', 'std_dev_in_stock_prices','created_at']
        return df
    else:
        return 'Error'