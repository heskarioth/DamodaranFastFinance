from datetime import datetime
import email
from typing import Optional
from pydantic import BaseModel, EmailStr,conint
#from app.db.database import Base



# sytem schemas

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserCreateOut(BaseModel):
    email : EmailStr
    created_at : datetime
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    email : Optional[str] = None



# ref items tables
class IndustryNameOut(BaseModel):
    pass

# corporate governance tab
class schema_inhold(BaseModel):
    industry_name : str
    number_of_firms : int
    ceo_holding : float
    institutional_holdings : float
    insider_holdings : float
    class Config:
        orm_mode = True



# capital structure tab

class schema_leaseeffect(BaseModel):
    industry_name : str
    number_of_firms : int
    lease_expenses_divided_by_sales_percentage : float
    total_debt_without_leases_usd : float
    lease_debt_as_percentage_of_total_debt : float
    market_debt_to_capital_without_leases_percentage : float
    market_debt_to_capital_with_leases_percentage : float
    book_debt_to_capital_without_leases_percentage : float
    book_debt_to_capital_with_leases_percentage : float
    operating_income_before_lease_adj_usd : float
    operating_income_after_lease_adj_usd : float
    roic_without_leases_percentage : float
    roic_with_leases_percentage : float
    pre_tax_operating_margin_before_lease_adj_percentage : float
    pre_tax_operating_margin_after_lease_adj : float
    lease_debt_my_estimate_usd : float
    lease_debt_accounting_usd : float
    created_at : datetime
    
    class Config:
        orm_mode = True
    


class schema_debtdetails(BaseModel):
    #__tablename__ : "debtdetails"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms: int
    lease_debt_my_estimate_usd : float
    conventional_debt_usd : float
    total_debt_with_leases_usd : float
    interest_expense_usd : float
    book_interest_rate_percentage : float
    short_term_debt_as_percentage_of_total_debt : float
    lease_debt_accounting_usd : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True
    

class schema_dbtfund(BaseModel):
    #__tablename__ : "dbtfund"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    book_deposit_to_capital_percentage : float
    market_debt_to_capital_unadjusted_percentage : float
    market_debt_equity_unadjusted_percentage : float
    market_debt_to_capital_adjusted_for_leases_percentage : float
    market_debt_equity_adjusted_for_leases_percentage : float
    effective_tax_rate_percentage : float
    institutional_holdings_percentage : float
    std_dev_in_stock_prices_percentage : float
    ebitda_divided_by_ev_percentage : float
    net_ppe_divided_by_total_assets_percentage : float
    capital_spending_divided_by_total_assets_percentage : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True





class schema_macro(BaseModel):
    date : int
    t_bond_rate_percentage : float
    change_in_rete_percentage : float
    real_gdp : float
    percentage_chg_in_gdp : float
    cpi_percentage : float
    change_in_cpi : float
    weighted_dollar : float
    percentage_change_in_dollar : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True

#cash divididend policy tab

class schema_divfund(BaseModel):
    #__tablename__ ="divfund"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    total_dividends_usd_millions : float
    special_dividends_as_percentage_of_total_dividends : float
    dividend_payout_percentage : float
    dividend_yield_percentage : float
    market_cap_usd_millions : float
    roe_percentage : float
    institutional_holdings_percentage : float
    std_dev_in_stock_prices : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True


class schema_divfcfe(BaseModel):
    #__tablename__ ="divfcfe"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    dividends : float
    net_income_usd : float
    payout_in_percentage : float
    dividends_plus_buybacks_usd : float
    cash_returns_as_percentage_of_net_income : float
    dividends_plus_buybacks_minus_stock_issuances_usd : float
    fcfe_before_debt_cash_flows_usd : float
    fcfe_after_debt_cash_flows_usd : float
    net_cash_returned_fcfe_pre_debt_percentage : float
    net_cash_returned_divided_by_fcfe_post_debt_percentage : float
    cash_divided_by_frim_value_percentage : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True

#cash flow estimation tab

class schema_capex(BaseModel):
    #__tablename__ ="capex"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    capital_expenditures_in_usd_millions : float
    depreciation_and_ammortization_in_usd_millions : float
    cap_ex_deprecn_in_percentage : float
    acquisitions_in_usd_millions : float
    net_r_d_in_usd_millions : float
    net_cap_exp_divided_by_sales_percentage : float
    net_cap_ex_divided_by_ebit_1_minus_t : float
    sales_invested_capital_ratio : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True


class schema_r_d(BaseModel):
    #__tablename__ ="r_d"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    r_d_capitalized_my_estimate_in_millions : float
    capitalized_r_d_as_percentage_of_invested_capital : float
    r_d_ltm_in_millions : float
    current_r_d_as_percentage_of_revenue : float
    r_d_one_year_ago_in_usd_millions : float
    r_d_two_years_ago_in_usd_millions : float
    r_d_three_years_ago_in_usd_millions : float
    r_d_four_years_ago_in_usd_millions : float
    r_d_five_years_ago_in_usd_millions : float
    cagr_in_r_d_last_five_years_in_percentage : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True


class schema_goodwill(BaseModel):
    #__tablename__ ="goodwill"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    goodwill_in_usd_millions : float
    change_in_goodwill_in_last_year_in_millions : float
    goodwill_as_percentage_of_total_asset : float
    impairment_of_goodwill_in_ltm_in_usd_millions : float
    impairment_as_percentage_of_goodwill : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True

class schema_margin(BaseModel):
    #__tablename__ ="margin"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    gross_margin_percentage : float
    net_margin_percentage : float
    pre_tax_pre_stock_compensation_operating_margin_percentage : float
    pre_tax_unadjusted_operating_margin_percentage : float
    after_tax_unadjusted_operating_margin_percentage : float
    pre_tax_lease_adjusted_margin_percentage : float
    after_tax_lease_adjusted_margin_percentage : float
    pre_tax_lease_r_d_adj_margin_percentage : float
    after_tax_lease_and_r_d_adj_margin_percentage : float
    ebitda_divided_by_sales_percentage : float
    ebitda_sga_dividend_by_sales_percentage : float
    ebitda_r_d_divided_by_sales_percentage : float
    cogs_divided_by_sales_percentage : float
    r_d_divided_by_sales : float
    sga_divided_by_sales_percentage : float
    stock_based_compensation_divided_by_sales_percentage : float
    lease_expense_divided_by_sales_percentage : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True


class schema_wcdata(BaseModel):
    #__tablename__ ="wcdata"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    accounts_receivable_sales : float
    inventory_sales : float
    accounts_payable_sales : float
    non_cash_wc_sales : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True

class schema_finflows(BaseModel):
    #__tablename__ : "finflows"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    dividends_in_usd_millions : float
    buybacks_in_usd_millions : float
    equity_issuance_in_usd_millions : float
    net_equity_change_in_usd_millions : float
    net_equity_change_as_percentage_of_book_equity : float
    debt_repaid_in_usd_millions : float
    debt_raised_in_usd_millions : float
    net_debt_change_in_usd_millions : float
    net_change_in_debt_as_percentage_of_total_debt : float
    change_in_lease_debt_in_usd_millions : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True

# tab for growth rate estimation
class schema_roe(BaseModel):
    #__tablename__ : "roe"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    roe_unadjusted : float
    roe_adjusted_for_r_and_d : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True

class schema_fundgr(BaseModel):
    #__tablename__ : "fundgr"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    retention_rate_percentage : float
    fundamental_growth_percentage : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True


class schema_histgr(BaseModel):
    #__tablename__ : "histgr"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    cagr_in_net_income_last_5_years_percentage : float
    cagr_in_revenues_last_5_years_percentage : float
    expected_growth_in_revenues_next_2_years_percentage : float
    expected_growth_in_eps_next_5_years_percentage : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True


class schema_fundgrEB(BaseModel):
    #__tablename__ : "fundgrEB"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    roc_percentage : float
    reinvestment_rate_percentage : float
    expected_growth_in_ebit_percentage : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True


    # tab for discount rates estimation 
class schema_histretSP(BaseModel):
    #__tablename__ : "histretSP"
    #id : Column(Integer,primary_key=True,nullable=False)
    year : int
    annual_roi_in_sp_500_includes_dividend_percentage : float
    annual_roi_in_3_month_t_bill_percentage : float
    annual_roi_in_us_t_bond_percentage : float
    annual_roi_in_baa_corporate_bond_percentage : float
    annual_roi_in_real_estate_percentage : float
    value_of_100_usd_invested_in_1928_sp_500_includes_dividends_usd : float
    value_of_100_usd_invested_in_1928_sp_3_moth_t_bill_4_usd : float
    value_of_100_usd_invested_in_1928_sp_us_t_bond_usd : float
    value_of_100_usd_invested_in_1928_sp_baa_corporate_bond_usd : float
    annual_risk_premium_real_estate_usd : float
    annual_risk_premium_stocks_minus_bills_percentage : float
    annual_risk_premium_stocks_minus_bonds_percentage : float
    annual_risk_premium_stocks_minus_baa_corporate_bond_percentage : float
    annual_risk_premium_historical_risk_premium_percentage : float
    inflation_rate_percentage : float
    annual_real_returns_on_sp_500_includes_dividend_percentage : float
    annual_real_returns_on_three_month_t_bill_real_percentage : float
    annual_real_returns_on_zero_year_t_bonds_percentage : float
    annual_real_returns_on_baa_corporate_bonds_percentage : float
    annual_real_returns_on_real_estate_percentage : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True

class schema_taxrate(BaseModel):
    #__tablename__ : "taxrate"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    total_taxable_income_usd : float
    taxes_total_taxes_paid_accrual_usd : float
    taxes_total_cash_taxes_paid_usd : float
    cash_taxes_divided_by_accrual_taxes_percentage : float
    effective_tax_rates_avg_across_all_companies_percentage : float
    effective_tax_rates_avg_across_only_money_making_componies_percentage : float
    effective_tax_rates_aggregate_tax_rate_percentage : float
    cash_tax_rates_avg_across_only_money_making_componies_percentage : float
    cash_tax_rates_aggregate_tax_rate_percentage : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True


class schema_countrytaxrates(BaseModel):
    #__tablename__ : "countrytaxrates"
    #id : Column(Integer,primary_key=True,nullable=False)
    country : str
    year_2016_percentage : float
    year_2017_percentage : float
    year_2018_percentage : float
    year_2019_percentage : float
    year_2020_percentage : float
    year_2021_percentage : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True

class schema_betas(BaseModel):
    #__tablename__ : "betas"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    beta : float
    debt_to_equity_ratio_percentage : float
    effective_tax_rate_percentage : float
    unlevered_beta : float
    cash_to_firm_value_percentage : float
    unlevered_beta_corrected_for_cash : float
    hilo_risk_percentage : float
    std_of_equity_percentage : float
    std_in_operating_income_last_10_years : float
    year_2018 : float
    year_2019 : float
    year_2020 : float
    year_2021 : float
    average_2017_22 : float
    #created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True

class schema_histimpl(BaseModel):
    #__tablename__ : "histimpl"
    #id : Column(Integer,primary_key=True,nullable=False)
    year : int
    earnings_yield_percentage : float
    dividend_yield_percentage : float
    sp_500 : float
    earnings : float
    dividends : float
    dividends_plus_buybacks : float
    change_in_earnings_percentage : float
    change_in_dividends_percentage : float
    t_bill_rate_percentage : float
    t_bond_rate_percentage : float
    bond_bill : float
    smoothed_growth_percentage : float
    implied_premium_ddm_percentage : float
    analytst_growth_estimate_percentage : float
    impled_erp_for_fcfe_percentage : float
    implied_premium_for_fcfe_with_sustainable_payout_percentage : float
    erp_riskfree_rate : float # ask professor what is that column
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True

class schema_ctryprem(BaseModel):
    #__tablename__ : "ctryprem"
    #id : Column(Integer,primary_key=True,nullable=False)
    country : str
    moodys_rating : str
    adj_default_spread : float
    country_risk_premium : float
    equity_risk_premium : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True


class schema_totalbeta(BaseModel):
    #__tablename__ : "totalbeta"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    average_unlevered_beta : float
    average_levered_beta : float
    average_correlation_with_market_percentage : float
    total_unlevered_beta : float
    total_levered_beta : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True


class schema_wacc(BaseModel):
    #__tablename__ : "wacc"
    #id : Column(Integer,primary_key=True,nullable=False)
    industry_name : str
    number_of_firms : int
    beta : float
    cost_of_equity_percentage : float
    equity_divided_by_debt_plus_equity_percentage : float
    std_dev_in_stock_percentage : float
    cost_of_debt_percentage : float
    tax_rate_percentage : float
    after_tax_cost_of_debt_percentage : float
    debt_divided_by_debt_plus_equity_percentage : float
    cost_of_capital_percentage : float
    # created_at : Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    class Config:
        orm_mode = True

























# def username_alphanumeric(cls, v):
#     assert v.isalnum(), 'must be alphanumeric'
#     return v


# validators : {
#     'username_validator':
#     validator('username')(username_alphanumeric)
# }

# UserModel : create_model(
#     'UserModel',
#     username=(str, ...),
#     __validators__=validators
# )

# user : UserModel(username='scolvin')
# print(user)
# #> username='scolvin'

# try:
#     UserModel(username='scolvi%n')
# except ValidationError as e:
#     print(e)
#     """
#     1 validation error for UserModel
#     username
#       must be alphanumeric (type=assertion_error)
#     """
