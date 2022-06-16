import pandas as pd
from ....config import etl_settings
import numpy as np
import pandas as pd
from datetime import datetime
import re 


def f_wcdata(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.wcdata,header=0)[0]
    validation_list = ['Industry Name', 'Number of firms', 'Acc  Rec/ Sales','Inventory/Sales', 'Acc  Pay/ Sales', 'Non-cash  WC/ Sales']
    if sum(df.columns == validation_list)==len(validation_list):
        for col in ['Acc  Rec/ Sales','Inventory/Sales', 'Acc  Pay/ Sales', 'Non-cash  WC/ Sales']:
            df[col]=df[col].str.replace('%','',regex=True).astype(np.float64)/100
        
        df['created_at'] = datetime.now()
        df.fillna(0,inplace=True)
        df.columns=['industry_name','number_of_firms','accounts_receivable_sales','inventory_sales','accounts_payable_sales','non_cash_wc_sales','created_at']
        return df

    else:
        return 'Error'



def f_finflows(data):

    def foo(x):
        is_negative = False if re.search('\(([^)]+)\)',x) == None else True
        x = x.replace('(','').replace(')','')
        if is_negative:
            return -1 * np.float64(x)
        else:
            return np.float64(x)
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.finflows,header=0)[0]
    validation_list = ['Industry Name', 'Number  of Firms', 'Dividends  in $ millions','Buybacks  in $ millions', 'Equity Issuance in $  millions','Net Equity  Change in $ millions','Net  Equity Change as % of Book Equity', 'Debt  Repaid in $ millions','Debt  Raised in $ millions', 'Net  Debt Change in $ millions','Net  Change in Debt as % of Total Debt','Change  in Lease Debt in $ millions']
    if sum(df.columns==validation_list)==len(validation_list):
        _  = ['Dividends  in $ millions','Buybacks  in $ millions','Debt  Repaid in $ millions','Equity Issuance in $  millions']
        for col in _:
            df[col] = df[col].str.replace('$','',regex=True).str.replace(',','').str.replace('-','0').astype(np.float64)
        _ = ['Net Equity  Change in $ millions','Debt  Raised in $ millions','Net  Debt Change in $ millions','Change  in Lease Debt in $ millions']
        for col in _:
            df[col] = df[col].str.replace('$','',regex=True).str.strip().str.replace(',','').str.replace('-','0').apply(foo)#astype(np.float64)
        _ = ['Net  Equity Change as % of Book Equity','Net  Change in Debt as % of Total Debt']
        for col in _:
            df[col] = df[col].str.replace('%','').astype(np.float64)/100
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name','number_of_firms','dividends_in_usd_millions','buybacks_in_usd_millions','equity_issuance_in_usd_millions','net_equity_change_in_usd_millions','net_equity_change_as_percentage_of_book_equity','debt_repaid_in_usd_millions','debt_raised_in_usd_millions','net_debt_change_in_usd_millions','net_change_in_debt_as_percentage_of_total_debt','change_in_lease_debt_in_usd_millions','created_at']

        return df
    else:
        return 'Error'

def f_margin(data): 
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.margin,header=0)[0]
    validation_list = ['Industry  Name', 'Number of firms', 'Gross Margin', 'Net Margin','Pre-tax, Pre-stock compensation  Operating Margin','Pre-tax Unadjusted Operating  Margin','After-tax Unadjusted Operating  Margin','Pre-tax Lease adjusted Margin', 'After-tax Lease Adjusted Margin','Pre-tax Lease & R&D adj  Margin', 'After-tax Lease & R&D  adj Margin','EBITDA/Sales', 'EBITDASG&A/Sales', 'EBITDAR&D/Sales', 'COGS/Sales','R&D/Sales', 'SG&A/ Sales', 'Stock-Based Compensation/Sales','Lease Expense/Sales']
    if sum(df.columns==validation_list)==len(validation_list):
        _ = ['Gross Margin', 'Net Margin','Pre-tax, Pre-stock compensation  Operating Margin','Pre-tax Unadjusted Operating  Margin','After-tax Unadjusted Operating  Margin','Pre-tax Lease adjusted Margin', 'After-tax Lease Adjusted Margin','Pre-tax Lease & R&D adj  Margin', 'After-tax Lease & R&D  adj Margin','EBITDA/Sales', 'EBITDASG&A/Sales', 'EBITDAR&D/Sales', 'COGS/Sales','R&D/Sales', 'SG&A/ Sales', 'Stock-Based Compensation/Sales','Lease Expense/Sales']
        for col in _:
            df[col] = df[col].str.replace('#DIV/0!','0%',regex=True).str.replace('%','',regex=True).astype(np.float64)/100
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name','number_of_firms','gross_margin_percentage','net_margin_percentage','pre_tax_pre_stock_compensation_operating_margin_percentage','pre_tax_unadjusted_operating_margin_percentage','after_tax_unadjusted_operating_margin_percentage','pre_tax_lease_adjusted_margin_percentage','after_tax_lease_adjusted_margin_percentage','pre_tax_lease_r_d_adj_margin_percentage','after_tax_lease_and_r_d_adj_margin_percentage','ebitda_divided_by_sales_percentage','ebitda_sga_dividend_by_sales_percentage','ebitda_r_d_divided_by_sales_percentage','cogs_divided_by_sales_percentage','r_d_divided_by_sales','sga_divided_by_sales_percentage','stock_based_compensation_divided_by_sales_percentage','lease_expense_divided_by_sales_percentage','created_at']
        return df
    else:
        return 'Error'

def f_goodwill(data):

    def foo(x):
            is_negative = False if re.search('\(([^)]+)\)',x) == None else True
            x = x.replace('(','').replace(')','')
            if is_negative:
                return -1 * np.float64(x)
            else:
                return np.float64(x)
    
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.goodwill,header=0)[0]
    
    validation_list = ['Industry Name', 'Number  of Firms', 'Goodwill  (in $ millions)','Change  in Goodwill in last year', 'Goodwill  as % of Total Assets','Impairment of Goodwill in LTM in $  millioins','Impairment as % of  Goodwill']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Goodwill  as % of Total Assets','Impairment as % of  Goodwill']:
            df[col] = df[col].str.replace('#DIV/0!','0').str.replace('-','0').str.replace('%','').astype(np.float64) /100
        for col in ['Goodwill  (in $ millions)','Impairment of Goodwill in LTM in $  millioins']:
            df[col] = df[col].str.replace('-','0',regex=True).str.strip().str.replace('$','',regex=True).str.replace(',','',regex=True).astype(np.float64)
        for col in ['Change  in Goodwill in last year']:
            df[col] = df[col].str.replace('$','',regex=True).str.strip().str.replace(',','',regex=True).str.replace('-','0',regex=True).apply(foo).astype(np.float64)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name','number_of_firms','goodwill_in_usd_millions','change_in_goodwill_in_last_year_in_millions','goodwill_as_percentage_of_total_asset','impairment_of_goodwill_in_ltm_in_usd_millions','impairment_as_percentage_of_goodwill','created_at']
        return df
    else:
        return 'Error'


def f_r_d(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.r_d,header=0)[0]
    validation_list = ['Industry Name', 'Number of firms','R&D Capitalized (my estimate in $ millions)','Capitalized R&D as % of Invested Capital', 'R&D - LTM (in $ millions)','Current R&D as % of Revenue', 'R&D - 1 year ago (in $ millions)','R&D - 2 years ago (in $ millions)','R&D - 3 years ago (in $ millions)', 'R&D - 4 years ago','R&D - 5 years ago (in $ millions)', 'CAGR  in R&D - Last 5 years']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['R&D Capitalized (my estimate in $ millions)','Capitalized R&D as % of Invested Capital', 'R&D - LTM (in $ millions)','Current R&D as % of Revenue', 'R&D - 1 year ago (in $ millions)','R&D - 2 years ago (in $ millions)','R&D - 3 years ago (in $ millions)', 'R&D - 4 years ago','R&D - 5 years ago (in $ millions)', 'CAGR  in R&D - Last 5 years']:
            df[col] = df[col].str.replace('#DIV/0!','0',regex=True).str.replace('-','0',regex=True).str.replace('%','',regex=True).str.replace('$','',regex=True).str.replace(',','',regex=True).astype(np.float64) #/100
        for col in ['Capitalized R&D as % of Invested Capital', 'Current R&D as % of Revenue','CAGR  in R&D - Last 5 years']:
            df[col] = df[col] / 100
        
        df['created_at'] = datetime.now()
        df.columns = ['industry_name','number_of_firms','r_d_capitalized_my_estimate_in_millions','capitalized_r_d_as_percentage_of_invested_capital','r_d_ltm_in_millions','current_r_d_as_percentage_of_revenue','r_d_one_year_ago_in_usd_millions','r_d_two_years_ago_in_usd_millions','r_d_three_years_ago_in_usd_millions','r_d_four_years_ago_in_usd_millions','r_d_five_years_ago_in_usd_millions','cagr_in_r_d_last_five_years_in_percentage','created_at']
        df.fillna(0,inplace=True)
        return df
    else:
        return 'Error'

def f_capex(data):
    df = pd.read_html(data,header=0)[0]
    #df = pd.read_html(etl_settings.capex,header=0)[0]
    validation_list = ['Industry  Name', 'Number of Firms','Capital Expenditures (US $  millions)','Depreciation & Amort  ((US $ millions)', 'Cap Ex/Deprecn','Acquisitions (US $ millions)', 'Net R&D (US $ millions)','Net Cap Ex/Sales', 'Net Cap Ex/ EBIT (1-t)','Sales/ Invested Capital']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Cap Ex/Deprecn','Net Cap Ex/Sales', 'Net Cap Ex/ EBIT (1-t)']:
            df[col] = df[col].str.replace('%','').astype(np.float64) / 100
        for col in ['Capital Expenditures (US $  millions)','Depreciation & Amort  ((US $ millions)','Acquisitions (US $ millions)', 'Net R&D (US $ millions)']:
            df[col] = df[col].str.replace('#DIV/0!','0',regex=True).str.replace('-','0',regex=True).str.replace('%','',regex=True).str.replace('$','',regex=True).str.replace(',','',regex=True).astype(np.float64) #/100
        
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms','capital_expenditures_in_usd_millions','depreciation_and_ammortization_in_usd_millions', 'cap_ex_deprecn_in_percentage','acquisitions_in_usd_millions', 'net_r_d_in_usd_millions','net_cap_exp_divided_by_sales_percentage', 'net_cap_ex_divided_by_ebit_1_minus_t', 'sales_invested_capital_ratio','created_at']
        df.fillna(0,inplace=True)
        return df
    else:
        return 'Error'
