import pandas as pd
from ....config import etl_settings
import numpy as np
import pandas as pd
from datetime import datetime

def percentage_remover(x):
    if isinstance(x,float):
        return x
    if isinstance(x,int):
        return x
    return np.float64(x.replace('%',''))/ 100

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

def dollar_adjuster_minus_blank(x):
    #example input string: -$  -  
    if isinstance(x,float):
        return x
    return np.float64(x.replace(',','').replace('$','').replace('-','0'))

def paranthesis_number(x):
    #example input $  (200.96)
    if isinstance(x,float):
        return x
    if isinstance(x,int):
        return x
    return -1 * np.float64(x.replace('$','').replace(' ','').replace('(','').replace(')','').replace(',',''))

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


def f_psdata(data):
    df = pd.read_html(data,header=0)[0]
    validation_list = ['Industry  Name', 'Number of firms', 'Price/Sales', 'Net Margin','EV/Sales', 'Pre-tax  Operating Margin']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Net Margin','Pre-tax  Operating Margin']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        
        df.columns = ['industry_name', 'number_of_firms', 'price_sales_ratio', 'net_margin_pct','ev_sales_ratio', 'pre_tax_operating_margin_pct','created_at']
        return df
    else:
        return 'Error'

def f_pedata(data):
    df = pd.read_html(data,header=0)[0]
    validation_list = ['Industry Name', 'Number of firms', 'Current PE', 'Trailing PE','Forward PE', 'Aggregate Mkt Cap/ Net Income (all firms)','Aggregate Mkt Cap/ Trailing Net Income (only money making  firms)','Expected growth in EPS - next 5 years', 'PEG Ratio']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Expected growth in EPS - next 5 years']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'current_pe', 'trailing_pe','forward_pe', 'aggregate_markcap_to_net_income_ratio_all_firms','aggregate_markcap_to_trailing_net_income_ratio_only_money_making_firms','exp_eps_growth_5_years', 'peg_ratio','created_at']
        return df
    else:
        return 'Error'



def f_pbvdata(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.histretSP,header=1)[0]
    validation_list = ['Industry Name', 'Number of firms', 'PBV', 'ROE','EV/  Invested Capital', 'ROIC']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['ROIC','ROE']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'pbv', 'roe_pct','ev_to_invested_capital_ratio', 'roic_pct','created_at']
        return df
    else:
        return 'Error'


def f_mktcapmult(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.histretSP,header=1)[0]
    validation_list = ['Market Cap Decile', 'Number of firms', 'PE', 'PBV', 'Price/Sales','EV/EBIT', 'EV/EBITDA', 'EV/Sales', 'EV/Invested Capital', 'ROE','Pre-tax ROIC', 'Net Margin', 'Operating Margin','% of companies with Net Income <0','% of companies with Operating income  <0']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['ROE','Pre-tax ROIC', 'Net Margin', 'Operating Margin','% of companies with Net Income <0','% of companies with Operating income  <0']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['markcap_decile','number_of_firms', 'pe', 'pbv', 'price_to_sales_ratio','ev_to_ebit_ratio', 'ev_to_ebitda_ratio', 'ev_to_sales_ratio', 'ev_to_invested_capital_ratio', 'roe_pct','pre_tax_roic_pct', 'net_margin_pct', 'operating_margin_pct','pct_companies_with_net_income_less_zero','pct_companies_with_operating_income_less_zero','created_at']
        
        return df
    else:
        return 'Error'




def f_countrystats(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.histretSP,header=1)[0]
    validation_list = ['Country', 'Number of firms', 'sum(Market Cap (in US $))','sum(Total Debt incl leases (in US $))', 'sum(Firm  Value (in US $))','sum(Cash)', 'sum(Enterprise Value (in US $))', 'median(Current PE)','median(Trailing PE)', 'median(Forward PE)', 'median(PEG)','median(PBV)', 'median(PS)', 'median(Cash/ Firm Value)','median(EV/EBIT)', 'median(EV/EBITDA)', 'median(EV/Invested Capital)','median(EV/Sales)', 'median(Payout ratio)', 'median(Dividend Yield)','median(Historical growth in Net Income - Last 5  years)','median(Historical growth in Revenues - Last 5  years)','median(Expected growth rate in EPS- Next 5  years)','median(Expected growth in revenues - Next 2  years)','median(Return on Equity)', 'median(Return on Capital (ROC or ROIC))','median(Net Profit Margin)', 'median(Pre-tax Operating Margin)','median(Effective Tax Rate)', 'median(% held by institutions)','Aggregate PE', 'Aggregate PBV', 'Aggregate EV/EBITDA','Aggregate EV/Invested Capital', 'Aggregate EV/Sales', 'Aggregate ROE','Aggregate ROC', 'Aggregate Net Margin', 'Aggregate Operating Margin','Aggregate Payout ratio', 'Aggregate Dividend Yield']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Aggregate PE', 'Aggregate PBV', 'Aggregate EV/EBITDA','Aggregate EV/Invested Capital', 'Aggregate EV/Sales', 'Aggregate ROE','Aggregate ROC', 'Aggregate Net Margin', 'Aggregate Operating Margin','Aggregate Payout ratio', 'Aggregate Dividend Yield','median(Cash/ Firm Value)','median(Payout ratio)', 'median(Dividend Yield)','median(Historical growth in Net Income - Last 5  years)','median(Historical growth in Revenues - Last 5  years)','median(Expected growth rate in EPS- Next 5  years)','median(Expected growth in revenues - Next 2  years)','median(Return on Equity)', 'median(Return on Capital (ROC or ROIC))','median(Net Profit Margin)', 'median(Pre-tax Operating Margin)','median(Effective Tax Rate)', 'median(% held by institutions)']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        for col in ['sum(Market Cap (in US $))','sum(Total Debt incl leases (in US $))', 'sum(Firm  Value (in US $))','sum(Cash)', 'sum(Enterprise Value (in US $))']:
            df[col] = df[col].apply(parenthesis_number_zero_minus)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['country', 'number_of_firms', 'sum_markcap_usd','sum_total_debt_incl_leases_usd', 'sum_firm_value_usd','sum_usd', 'sum_enterprise_value_usd', 'median_current_pe','median_trailing_pe', 'median_forward_pe', 'median_peg','median_pbv', 'median_ps', 'median_cash_to_firm_value_pct','median_ev_to_ebit', 'median_ev_to_ebitda', 'median_ev_to_invested_capital','median_ev_to_sales', 'median_payout_ratio_pct', 'median_dividend_yield_pct','median_hist_growth_net_income_last_5_years_pct','median_hist_growth_revenues_last_5_years_pct','median_exp_growth_rate_eps_next_5_years_pct','median_exp_growth_revenues_next_2_years_pct','median_return_on_equity_pct', 'median_return_on_capital_pct','median_net_profit_margin_pct', 'median_pre_tax_operating_margin_pct','median_effective_tax_rate_pct', 'median_pct_held_by_institutions','aggr_pe', 'aggr_pbv', 'aggr_ev_to_ebitda','aggr_ev_to_invested_capital', 'aggr_ev_to_sales', 'agrr_roe_pct','aggr_roc_pct', 'aggr_net_margin_pct', 'aggr_operating_margin_pct','aggr_payout_ratio_pct', 'aggr_dividend_yield','created_at']
        return df
    else:
        return 'Error'


def f_vebitda(data):
    df = pd.read_html(data,header=1)[0]
    #df = pd.read_html(etl_settings.histretSP,header=1)[0]
    validation_list = ['Industry Name', 'Number of firms', 'EV/EBITDAR&D', 'EV/EBITDA','EV/EBIT', 'EV/EBIT (1-t)', 'EV/EBITDAR&D2', 'EV/EBITDA3', 'EV/EBIT4','EV/EBIT (1-t)5']
    if sum(df.columns==validation_list)==len(validation_list):
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'positive_ebitda_firms_ev_to_ebitdar_d', 'positive_ebitda_firms_ev_to_ebitda','positive_ebitda_firms_ev_to_ebit', 'positive_ebitda_firms_ev_to_ebit_1_minus_t', 'all_firms_ev_to_ebitdar_d_2', 'all_firms_ev_to_ebitda3', 'all_firms_ev_to_ebit4','all_firms_ev_to_ebit_1_minus_t_5','created_at']
        return df
    else:
        return 'Error'