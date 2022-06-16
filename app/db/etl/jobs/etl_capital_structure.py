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


def f_macro(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.macro,header=0)[0]
    validation_list = ['Date', 'T.Bond  Rate', 'Change  in rate', 'Real  GDP', '%  Chg in GDP','CPI', 'Change  in CPI', 'Weighted  Dollar', '%  Change in $']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['T.Bond  Rate', 'Change  in rate', 'Real  GDP', '%  Chg in GDP','CPI', 'Change  in CPI', '%  Change in $','Weighted  Dollar']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['date', 't_bond_rate_percentage','change_in_rete_percentage', 'real_gdp', 'percentage_chg_in_gdp','cpi_percentage', 'change_in_cpi', 'weighted_dollar', 'percentage_change_in_dollar','created_at']
        return df
    else:
        return 'Error'


def f_dbtfund(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.dbtfund,header=0)[0]
    validation_list = ['Industry  Name', 'Number of  firms', 'Book Debt  to Capital','Market  Debt to Capital (Unadjusted)', 'Market D/E  (unadjusted)','Market  Debt to Capital (adjusted for leases)','Market D/E  (adjusted for leases)', 'Effective  tax rate','Institutional  Holdings', 'Std dev in  Stock Prices', 'EBITDA/EV','Net PP&E/Total  Assets', 'Capital Spending/Total  Assets']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Number of  firms', 'Book Debt  to Capital','Market  Debt to Capital (Unadjusted)', 'Market D/E  (unadjusted)','Market  Debt to Capital (adjusted for leases)','Market D/E  (adjusted for leases)', 'Effective  tax rate','Institutional  Holdings', 'Std dev in  Stock Prices', 'EBITDA/EV','Net PP&E/Total  Assets', 'Capital Spending/Total  Assets']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'book_deposit_to_capital_percentage','market_debt_to_capital_unadjusted_percentage', 'market_debt_equity_unadjusted_percentage','market_debt_to_capital_adjusted_for_leases_percentage','market_debt_equity_adjusted_for_leases_percentage', 'effective_tax_rate_percentage','institutional_holdings_percentage', 'std_dev_in_stock_prices_percentage', 'ebitda_divided_by_ev_percentage','net_ppe_divided_by_total_assets_percentage', 'capital_spending_divided_by_total_assets_percentage','created_at']
        return df
    else:
        return 'Error'

def f_debtdetails(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.debtdetails,header=0)[0]
    validation_list = ['Industry Name', 'Number of firms', 'Lease Debt (My Estimate)','Conventional Debt', 'Total Debt with leases', 'Interest expense','Book interest rate', 'Short term Debt as % of Total Debt','Lease Debt (Accounting)']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Book interest rate', 'Short term Debt as % of Total Debt']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        #for col in ['Total Dividends (US $ millions)', 'Market Cap (US $ millions)']:
        #     df[col] = df[col].apply(dollar_adjuster_minus_blank)
        for col in ['Lease Debt (My Estimate)','Conventional Debt', 'Total Debt with leases', 'Interest expense','Lease Debt (Accounting)']:
            df[col] = df[col].apply(dollar_adjuster_minus_blank)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'lease_debt_my_estimate_usd','conventional_debt_usd', 'total_debt_with_leases_usd', 'interest_expense_usd','book_interest_rate_percentage', 'short_term_debt_as_percentage_of_total_debt','lease_debt_accounting_usd', 'created_at']
        return df
    else:
        return 'Error'

def f_leaseeffect(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.leaseeffect,header=0)[0]
    validation_list = ['Industry Name', 'Number of firms', 'Lease Expense/ Sales','Total Debt without leases', 'Total Debt with Leases','Lease Debt as % of Total Debt','Market Debt to Capital without leases','Market Debt to Capital with leases','Book Debt to Capital without leases','Book Debt to Capital with leases','Operating income (before lease adj)','Operating income (after lease adj)', 'ROIC (without leases)','ROIC (with leases)', 'Pre-tax Operating Margin (before lease adj)','Pre-tax Operating Margin (after lease adj)','Lease Debt (My Estimate)', 'Lease Debt (Accounting)']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Lease Expense/ Sales','Lease Debt as % of Total Debt','Market Debt to Capital without leases','Market Debt to Capital with leases','Book Debt to Capital without leases','Book Debt to Capital with leases','ROIC (without leases)','ROIC (with leases)', 'Pre-tax Operating Margin (before lease adj)','Pre-tax Operating Margin (after lease adj)']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        for col in ['Total Debt without leases', 'Total Debt with Leases','Operating income (before lease adj)','Operating income (after lease adj)','Lease Debt (My Estimate)', 'Lease Debt (Accounting)']:
             df[col] = df[col].apply(dollar_adjuster_minus_blank)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'lease_expenses_divided_by_sales_percentage','total_debt_without_leases_usd', 'total_debt_with_leases_usd','lease_debt_as_percentage_of_total_debt','market_debt_to_capital_without_leases_percentage',
'market_debt_to_capital_with_leases_percentage','book_debt_to_capital_without_leases_percentage','book_debt_to_capital_with_leases_percentage','operating_income_before_lease_adj_usd','operating_income_after_lease_adj_usd', 'roic_without_leases_percentage','roic_with_leases_percentage',
'pre_tax_operating_margin_before_lease_adj_percentage','pre_tax_operating_margin_after_lease_adj','lease_debt_my_estimate_usd','lease_debt_accounting_usd','created_at']
        return df
    else:
        return 'Error'
