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


def f_histimpl():
    df = pd.read_html(etl_settings.histimpl,header=0)[0]
    validation_list = ['Year', 'Earnings Yield', 'Dividend Yield', 'S&P 500', 'Earnings*','Dividends*', 'Dividends + Buybacks', 'Change in Earnings','Change in Dividends', 'T.Bill Rate', 'T.Bond Rate', 'Bond-Bill','Smoothed Growth', 'Implied Premium (DDM)', 'Analyst Growth Estimate','Implied ERP (FCFE)', 'Implied Premium (FCFE with sustainable Payout)','ERP/Riskfree Rate']
    if sum(df.columns == validation_list)==len(validation_list):
        _ = ['Earnings Yield', 'Dividend Yield','Change in Earnings','Change in Dividends','T.Bill Rate','T.Bond Rate','Smoothed Growth','Implied Premium (DDM)','Analyst Growth Estimate','Implied ERP (FCFE)','Implied Premium (FCFE with sustainable Payout)','Bond-Bill']
        for col in df[_]:
            df[col] = df[col].str.replace('%','',regex=True).astype(np.float64)/100

        df.fillna(0,inplace=True)
        df.rename(columns=lambda x: str(x)+"_%" if x in _ else x,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['year','earnings_yield_percentage','dividend_yield_percentage','sp_500','earnings','dividends','dividends_plus_buybacks',
    'change_in_earnings_percentage', 'change_in_dividends_percentage', 't_bill_rate_percentage', 't_bond_rate_percentage', 'bond_bill','smoothed_growth_percentage','implied_premium_ddm_percentage','analytst_growth_estimate_percentage', 'impled_erp_for_fcfe_percentage','implied_premium_for_fcfe_with_sustainable_payout_percentage', 'erp_riskfree_rate','created_at']

        return df
    else:
        return 'Error'


def f_wacc():
    df = pd.read_html(etl_settings.wacc,header=0)[0]
    validation_list = ['Industry  Name', 'Number of Firms', 'Beta', 'Cost of Equity','E/(D+E)', 'Std Dev in Stock', 'Cost of Debt', 'Tax Rate','After-tax Cost of Debt', 'D/(D+E)', 'Cost of Capital']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Cost of Equity','E/(D+E)', 'Std Dev in Stock', 'Cost of Debt', 'Tax Rate','After-tax Cost of Debt', 'D/(D+E)', 'Cost of Capital']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
#         for col in ['Total Debt without leases', 'Total Debt with Leases','Operating income (before lease adj)','Operating income (after lease adj)','Lease Debt (My Estimate)', 'Lease Debt (Accounting)']:
#              df[col] = df[col].apply(dollar_adjuster_minus_blank)
        #for col in ['Lease Debt (My Estimate)','Conventional Debt', 'Total Debt with leases', 'Interest expense','Lease Debt (Accounting)']:
        #    df[col] = df[col].apply(dollar_adjuster_minus_blank)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'beta', 'cost_of_equity_percentage','equity_divided_by_debt_plus_equity_percentage', 'std_dev_in_stock_percentage', 'cost_of_debt_percentage', 'tax_rate_percentage','after_tax_cost_of_debt_percentage', 'debt_divided_by_debt_plus_equity_percentage', 'cost_of_capital_percentage','created_at']
        return df
    else:
        return 'Error'

def f_totalbeta():
    df = pd.read_html(etl_settings.totalbeta,header=0)[0]
    validation_list = ['Industry Name', 'Number of firms', 'Average Unlevered Beta','Average Levered Beta', 'Average correlation with the market','Total Unlevered Beta', 'Total Levered Beta']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Average correlation with the market']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name', 'number_of_firms', 'average_unlevered_beta','average_levered_beta', 'average_correlation_with_market_percentage','total_unlevered_beta', 'total_levered_beta', 'created_at']
        return df
    else:
        return 'Error'

def f_ctryprem():
    df = pd.read_html(etl_settings.ctryprem,header=0)[0]
    validation_list = ['Country', 'Moody\'s rating', 'Adj. Default  Spread','Country Risk  Premium', 'Equity Risk  Premium','Country Risk  Premium.1']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Adj. Default  Spread','Country Risk  Premium', 'Equity Risk  Premium','Country Risk  Premium.1']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.drop('Country Risk  Premium.1',axis=1,inplace=True)
        df.columns = ['country', 'moodys_rating', 'adj_default_spread','country_risk_premium', 'equity_risk_premium','created_at']
        return df
    else:
        return 'Error'

def f_betas():
    df = pd.read_html(etl_settings.betas,header=0)[0]
    validation_list = ['Industry Name', 'Number of firms', 'Beta', 'D/E Ratio','Effective Tax rate', 'Unlevered beta', 'Cash/Firm value','Unlevered beta corrected for cash', 'HiLo Risk','Standard deviation of equity','Standard deviation in operating income (last 10  years)', '2018','2019', '2020', '2021', 'Average (2017-22)']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['D/E Ratio','Effective Tax rate', 'Cash/Firm value','Standard deviation of equity','Standard deviation in operating income (last 10  years)']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        
        df.columns = ['industry_name', 'number_of_firms', 'beta', 'debt_to_equity_ratio_percentage','effective_tax_rate_percentage', 'unlevered_beta', 'cash_to_firm_value_percentage','unlevered_beta_corrected_for_cash', 'hilo_risk_percentage','std_of_equity_percentage','std_in_operating_income_last_10_years', 'year_2018','year_2019', 'year_2020', 'year_2021', 'average_2017_22', 'created_at']
        return df
    else:
        return 'Error'

def f_countrytaxrates():
    df = pd.read_html(etl_settings.countrytaxrates,header=0)[0]
    validation_list = ['Country', '2016', '2017', '2018', '2019', '2020', '2021']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['2016', '2017', '2018', '2019', '2020', '2021']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        
        df.columns = ['country', 'year_2016_percentage', 'year_2017_percentage', 'year_2018_percentage', 'year_2019_percentage', 'year_2020_percentage', 'year_2021_percentage','created_at']
        return df
    else:
        return 'Error'






def f_taxrate():
    df = pd.read_html(etl_settings.taxrate,header=1)[0]
    validation_list = ['Industry  name', 'Number of firms', 'Total Taxable Income','Total Taxes Paid (Accrual)', 'Total Cash Taxes Paid','Cash Taxes/Accrual Taxes', 'Average across all companies','Average across only  money-making companies', 'Aggregate tax rate','Average across only  money-making companies2', 'Aggregate tax rate3']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['Cash Taxes/Accrual Taxes', 'Average across all companies','Average across only  money-making companies', 'Aggregate tax rate','Average across only  money-making companies2', 'Aggregate tax rate3']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        for col in [ 'Total Taxable Income','Total Taxes Paid (Accrual)', 'Total Cash Taxes Paid']:
            df[col] = df[col].apply(dollar_adjuster_minus_blank)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['industry_name','number_of_firms','total_taxable_income_usd','taxes_total_taxes_paid_accrual_usd','taxes_total_cash_taxes_paid_usd','cash_taxes_divided_by_accrual_taxes_percentage','effect_tax_rates_avg_all_companies_percent','effect_tax_rates_avg_money_making_firms_percent','effect_tax_rates_aggregate_tax_rate_percentage','cash_tax_rates_avg_money_making_firms_percent','cash_tax_rates_aggregate_tax_rate_percentage','created_at']
        return df
    else:
        return 'Error'

def f_histretSP():
    df = pd.read_html(etl_settings.histretSP,header=1)[0]
    validation_list = ['Year', 'S&P 500 (includes dividends)', '3-month T.Bill', 'US T. Bond','Baa  Corporate Bond', 'Real Estate', 'S&P 500 (includes dividends)3','3-month T.Bill4', 'US T. Bond5', 'Baa  Corporate Bond6','Real Estate2', 'Stocks  - Bills', 'Stocks  - Bonds','Stocks  - Baa Corp Bond', 'Historical  risk premium','Inflation  Rate', 'S&P  500 (includes dividends)2','3-month  T. Bill (Real)', '!0-year  T.Bonds', 'Baa  Corp Bonds','Real  Estate3']
    if sum(df.columns==validation_list)==len(validation_list):
        for col in ['S&P 500 (includes dividends)', '3-month T.Bill', 'US T. Bond', 'Real Estate','Stocks  - Bills', 'Stocks  - Bonds','Stocks  - Baa Corp Bond','Historical  risk premium','Inflation  Rate','S&P  500 (includes dividends)2','3-month  T. Bill (Real)', '!0-year  T.Bonds', 'Baa  Corp Bonds','Real  Estate3','Baa  Corporate Bond']:
            df[col] = df[col].apply(percentage_remover_with_div_0)
        for col in [ 'S&P 500 (includes dividends)3','3-month T.Bill4', 'US T. Bond5', 'Baa  Corporate Bond6','Real Estate2']:
            df[col] = df[col].apply(dollar_adjuster_minus_blank)
        df.fillna(0,inplace=True)
        df['created_at'] = datetime.now()
        df.columns = ['year','annual_roi_in_sp_500_includes_dividend_percentage','annual_roi_in_3_month_t_bill_percentage','annual_roi_in_us_t_bond_percentage','annual_roi_in_baa_corporate_bond_percentage','annual_roi_in_real_estate_percentage','value_of_100_usd_invested_in_1928_sp_500_includes_dividends_usd','value_of_100_usd_invested_in_1928_sp_3_moth_t_bill_4_usd','value_of_100_usd_invested_in_1928_sp_us_t_bond_usd','value_of_100_usd_invested_in_1928_sp_baa_corporate_bond_usd','annual_risk_premium_real_estate_usd','annual_risk_premium_stocks_minus_bills_percentage','annual_risk_premium_stocks_minus_bonds_percentage','annual_risk_premium_stocks_minus_baa_corporate_bond_percentage','annual_risk_premium_historical_risk_premium_percentage','inflation_rate_percentage','annual_real_returns_on_sp_500_includes_dividend_percentage','annual_real_returns_on_three_month_t_bill_real_percentage','annual_real_returns_on_zero_year_t_bonds_percentage','annual_real_returns_on_baa_corporate_bonds_percentage','annual_real_returns_on_real_estate_percentage','created_at']
        return df
    else:
        return 'Error'