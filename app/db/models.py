import sys
from time import timezone
from sqlalchemy import TIMESTAMP, Column,Integer, PrimaryKeyConstraint,String,Boolean,null, Float
from sqlalchemy.sql.expression import text 
from sqlalchemy.orm import relationship, Session
from .database import Base


class table_users(Base):
    __tablename__ = "backend_users"
    email = Column(String,primary_key=True,nullable=False)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    role = Column(String,nullable=True)


class table_backend_refresh_schedules(Base):
    __tablename__ = "backend_schedules"
    id = Column(Integer,primary_key=True)
    datafeed_name = Column(String,nullable=False)
    lastupdate_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    datefeed_url = Column(String,nullable=False)

class table_ref_industry_names(Base):
    __tablename__ = "ref_items_industry_name"
    id = Column(Integer,primary_key=True)
    company_name = Column(String,nullable=False)
    exchange_ticker = Column(String,nullable=False)
    industry_group = Column(String,nullable=False)
    primary_sector = Column(String,nullable=False)
    sic_code = Column(String,nullable=False)
    country = Column(String,nullable=False)
    broad_group = Column(String,nullable=False)
    sub_group = Column(String,nullable=False)
    ticker = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class table_ref_bonds(Base):
    __tablename__ = "ref_bonds"
    id = Column(Integer,primary_key=True)
    country = Column(String,nullable=False)
    yield_converted = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


# corporate governance tab
class table_inhold(Base):
    __tablename__ = "inhold"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms = Column(Integer,nullable=False)
    ceo_holding = Column(Float,nullable=False)
    institutional_holdings = Column(Float,nullable=False)
    insider_holdings=Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))



# capital structure tab

class table_leaseeffect(Base):
    __tablename__ = "leaseeffect"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms=Column(Integer,nullable=False)
    lease_expenses_divided_by_sales_percentage = Column(Float,nullable=False)
    total_debt_without_leases_usd = Column(Float,nullable=False)
    lease_debt_as_percentage_of_total_debt = Column(Float,nullable=False)
    market_debt_to_capital_without_leases_percentage = Column(Float,nullable=False)
    market_debt_to_capital_with_leases_percentage = Column(Float,nullable=False)
    book_debt_to_capital_without_leases_percentage = Column(Float,nullable=False)
    book_debt_to_capital_with_leases_percentage = Column(Float,nullable=False)
    operating_income_before_lease_adj_usd = Column(Float,nullable=False)
    operating_income_after_lease_adj_usd = Column(Float,nullable=False)
    roic_without_leases_percentage = Column(Float,nullable=False)
    roic_with_leases_percentage = Column(Float,nullable=False)
    pre_tax_operating_margin_before_lease_adj_percentage = Column(Float,nullable=False)
    pre_tax_operating_margin_after_lease_adj = Column(Float,nullable=False)
    lease_debt_my_estimate_usd = Column(Float,nullable=False)
    lease_debt_accounting_usd = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class table_debtdetails(Base):
    __tablename__ = "debtdetails"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms=Column(Integer,nullable=False)
    lease_debt_my_estimate_usd = Column(Float,nullable=False)
    conventional_debt_usd = Column(Float,nullable=False)
    total_debt_with_leases_usd = Column(Float,nullable=False)
    interest_expense_usd = Column(Float,nullable=False)
    book_interest_rate_percentage = Column(Float,nullable=False)
    short_term_debt_as_percentage_of_total_debt = Column(Float,nullable=False)
    lease_debt_accounting_usd = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class table_dbtfund(Base):
    __tablename__ = "dbtfund"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms=Column(Integer,nullable=False)
    book_deposit_to_capital_percentage = Column(Float,nullable=False)
    market_debt_to_capital_unadjusted_percentage = Column(Float,nullable=False)
    market_debt_equity_unadjusted_percentage = Column(Float,nullable=False)
    market_debt_to_capital_adjusted_for_leases_percentage = Column(Float,nullable=False)
    market_debt_equity_adjusted_for_leases_percentage = Column(Float,nullable=False)
    effective_tax_rate_percentage = Column(Float,nullable=False)
    institutional_holdings_percentage = Column(Float,nullable=False)
    std_dev_in_stock_prices_percentage = Column(Float,nullable=False)
    ebitda_divided_by_ev_percentage = Column(Float,nullable=False)
    net_ppe_divided_by_total_assets_percentage = Column(Float,nullable=False)
    capital_spending_divided_by_total_assets_percentage = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))





class table_macro(Base):
    __tablename__ = "macro"
    id = Column(Integer,primary_key=True,nullable=False)
    date = Column(Integer,nullable=False)
    t_bond_rate_percentage = Column(Float,nullable=False)
    change_in_rete_percentage = Column(Float,nullable=False)
    real_gdp = Column(Float,nullable=False)
    percentage_chg_in_gdp = Column(Float,nullable=False)
    cpi_percentage = Column(Float,nullable=False)
    change_in_cpi = Column(Float,nullable=False)
    weighted_dollar = Column(Float,nullable=False)
    percentage_change_in_dollar = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

#cash divididend policy tab

class table_divfund(Base):
    __tablename__ ="divfund"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms=Column(Integer,nullable=False)
    total_dividends_usd_millions = Column(Float,nullable=False)
    special_dividends_as_percentage_of_total_dividends = Column(Float,nullable=False)
    dividend_payout_percentage = Column(Float,nullable=False)
    dividend_yield_percentage = Column(Float,nullable=False)
    market_cap_usd_millions = Column(Float,nullable=False)
    roe_percentage = Column(Float,nullable=False)
    institutional_holdings_percentage = Column(Float,nullable=False)
    std_dev_in_stock_prices = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    

class table_divfcfe(Base):
    __tablename__ ="divfcfe"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms=Column(Integer,nullable=False)
    dividends = Column(Float,nullable=False)
    net_income_usd = Column(Float,nullable=False)
    payout_in_percentage = Column(Float,nullable=False)
    dividends_plus_buybacks_usd = Column(Float,nullable=False)
    cash_returns_as_percentage_of_net_income = Column(Float,nullable=False)
    dividends_plus_buybacks_minus_stock_issuances_usd = Column(Float,nullable=False)
    fcfe_before_debt_cash_flows_usd = Column(Float,nullable=False)
    fcfe_after_debt_cash_flows_usd = Column(Float,nullable=False)
    net_cash_returned_fcfe_pre_debt_percentage = Column(Float,nullable=False)
    net_cash_returned_divided_by_fcfe_post_debt_percentage = Column(Float,nullable=False)
    cash_divided_by_frim_value_percentage = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

#cash flow estimation tab

class table_capex(Base):
    __tablename__ ="capex"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms=Column(Integer,nullable=False)
    capital_expenditures_in_usd_millions = Column(Float,nullable=False)
    depreciation_and_ammortization_in_usd_millions = Column(Float,nullable=False)
    cap_ex_deprecn_in_percentage = Column(Float,nullable=False)
    acquisitions_in_usd_millions = Column(Float,nullable=False)
    net_r_d_in_usd_millions = Column(Float,nullable=False)
    net_cap_exp_divided_by_sales_percentage = Column(Float,nullable=False)
    net_cap_ex_divided_by_ebit_1_minus_t = Column(Float,nullable=False)
    sales_invested_capital_ratio = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class table_r_d(Base):
    __tablename__ ="r_d"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms=Column(Integer,nullable=False)
    r_d_capitalized_my_estimate_in_millions = Column(Float,nullable=False)
    capitalized_r_d_as_percentage_of_invested_capital = Column(Float,nullable=False)
    r_d_ltm_in_millions = Column(Float,nullable=False)
    current_r_d_as_percentage_of_revenue = Column(Float,nullable=False)
    r_d_one_year_ago_in_usd_millions = Column(Float,nullable=False)
    r_d_two_years_ago_in_usd_millions = Column(Float,nullable=False)
    r_d_three_years_ago_in_usd_millions = Column(Float,nullable=False)
    r_d_four_years_ago_in_usd_millions = Column(Float,nullable=False)
    r_d_five_years_ago_in_usd_millions = Column(Float,nullable=False)
    cagr_in_r_d_last_five_years_in_percentage = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))



class table_goodwill(Base):
    __tablename__ ="goodwill"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms=Column(Integer,nullable=False)
    goodwill_in_usd_millions = Column(Float,nullable=False)
    change_in_goodwill_in_last_year_in_millions = Column(Float,nullable=False)
    goodwill_as_percentage_of_total_asset = Column(Float,nullable=False)
    impairment_of_goodwill_in_ltm_in_usd_millions = Column(Float,nullable=False)
    impairment_as_percentage_of_goodwill = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class table_margin(Base):
    __tablename__ ="margin"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms=Column(Integer,nullable=False)
    gross_margin_percentage = Column(Float,nullable=False)
    net_margin_percentage = Column(Float,nullable=False)
    pre_tax_pre_stock_compensation_operating_margin_percentage = Column(Float,nullable=False)
    pre_tax_unadjusted_operating_margin_percentage = Column(Float,nullable=False)
    after_tax_unadjusted_operating_margin_percentage = Column(Float,nullable=False)
    pre_tax_lease_adjusted_margin_percentage = Column(Float,nullable=False)
    after_tax_lease_adjusted_margin_percentage = Column(Float,nullable=False)
    pre_tax_lease_r_d_adj_margin_percentage = Column(Float,nullable=False)
    after_tax_lease_and_r_d_adj_margin_percentage = Column(Float,nullable=False)
    ebitda_divided_by_sales_percentage = Column(Float,nullable=False)
    ebitda_sga_dividend_by_sales_percentage = Column(Float,nullable=False)
    ebitda_r_d_divided_by_sales_percentage = Column(Float,nullable=False)
    cogs_divided_by_sales_percentage = Column(Float,nullable=False)
    r_d_divided_by_sales = Column(Float,nullable=False)
    sga_divided_by_sales_percentage = Column(Float,nullable=False)
    stock_based_compensation_divided_by_sales_percentage = Column(Float,nullable=False)
    lease_expense_divided_by_sales_percentage = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))



class table_wcdata(Base):
    __tablename__ ="wcdata"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms=Column(Integer,nullable=False)
    accounts_receivable_sales = Column(Float,nullable=False)
    inventory_sales = Column(Float,nullable=False)
    accounts_payable_sales = Column(Float,nullable=False)
    non_cash_wc_sales = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class table_finflows(Base):
    __tablename__ = "finflows"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms = Column(Integer,nullable=False)
    dividends_in_usd_millions = Column(Float,nullable=False)
    buybacks_in_usd_millions = Column(Float,nullable=False)
    equity_issuance_in_usd_millions = Column(Float,nullable=False)
    net_equity_change_in_usd_millions = Column(Float,nullable=False)
    net_equity_change_as_percentage_of_book_equity = Column(Float,nullable=False)
    debt_repaid_in_usd_millions = Column(Float,nullable=False)
    debt_raised_in_usd_millions = Column(Float,nullable=False)
    net_debt_change_in_usd_millions = Column(Float,nullable=False)
    net_change_in_debt_as_percentage_of_total_debt = Column(Float,nullable=False)
    change_in_lease_debt_in_usd_millions = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    

# tab for growth rate estimation
class table_roe(Base):
    __tablename__ = "roe"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms = Column(Integer,nullable=False)
    roe_unadjusted = Column(Float,nullable=False)
    roe_adjusted_for_r_and_d = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class table_fundgr(Base):
    __tablename__ = "fundgr"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms = Column(Integer,nullable=False)
    retention_rate_percentage = Column(Float,nullable=False)
    fundamental_growth_percentage = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class table_histgr(Base):
    __tablename__ = "histgr"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms = Column(Integer,nullable=False)
    cagr_in_net_income_last_5_years_percentage = Column(Float,nullable=False)
    cagr_in_revenues_last_5_years_percentage = Column(Float,nullable=False)
    expected_growth_in_revenues_next_2_years_percentage = Column(Float,nullable=False)
    expected_growth_in_eps_next_5_years_percentage = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class table_fundgrEB(Base):
    __tablename__ = "fundgrEB"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms = Column(Integer,nullable=False)
    roc_percentage = Column(Float,nullable=False)
    reinvestment_rate_percentage = Column(Float,nullable=False)
    expected_growth_in_ebit_percentage = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

    # tab for discount rates estimation 
class table_histretSP(Base):
    __tablename__ = "histretSP"
    id = Column(Integer,primary_key=True,nullable=False)
    year = Column(Integer,nullable=False)
    annual_roi_in_sp_500_includes_dividend_percentage = Column(Float,nullable=False)
    annual_roi_in_3_month_t_bill_percentage = Column(Float,nullable=False)
    annual_roi_in_us_t_bond_percentage = Column(Float,nullable=False)
    annual_roi_in_baa_corporate_bond_percentage = Column(Float,nullable=False)
    annual_roi_in_real_estate_percentage = Column(Float,nullable=False)
    value_of_100_usd_invested_in_1928_sp_500_includes_dividends_usd = Column(Float,nullable=False)
    value_of_100_usd_invested_in_1928_sp_3_moth_t_bill_4_usd = Column(Float,nullable=False)
    value_of_100_usd_invested_in_1928_sp_us_t_bond_usd = Column(Float,nullable=False)
    value_of_100_usd_invested_in_1928_sp_baa_corporate_bond_usd = Column(Float,nullable=False)
    annual_risk_premium_real_estate_usd = Column(Float,nullable=False)
    annual_risk_premium_stocks_minus_bills_percentage = Column(Float,nullable=False)
    annual_risk_premium_stocks_minus_bonds_percentage = Column(Float,nullable=False)
    annual_risk_premium_stocks_minus_baa_corporate_bond_percentage = Column(Float,nullable=False)
    annual_risk_premium_historical_risk_premium_percentage = Column(Float,nullable=False)
    inflation_rate_percentage = Column(Float,nullable=False)
    annual_real_returns_on_sp_500_includes_dividend_percentage = Column(Float,nullable=False)
    annual_real_returns_on_three_month_t_bill_real_percentage = Column(Float,nullable=False)
    annual_real_returns_on_zero_year_t_bonds_percentage = Column(Float,nullable=False)
    annual_real_returns_on_baa_corporate_bonds_percentage = Column(Float,nullable=False)
    annual_real_returns_on_real_estate_percentage = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class table_taxrate(Base):
    __tablename__ = "taxrate"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms = Column(Integer,nullable=False)
    total_taxable_income_usd = Column(Float,nullable=False)
    taxes_total_taxes_paid_accrual_usd = Column(Float,nullable=False)
    taxes_total_cash_taxes_paid_usd = Column(Float,nullable=False)
    cash_taxes_divided_by_accrual_taxes_percentage = Column(Float,nullable=False)
    effect_tax_rates_avg_all_companies_percent = Column(Float,nullable=False)
    effect_tax_rates_avg_money_making_firms_percent = Column(Float,nullable=False)
    effect_tax_rates_aggregate_tax_rate_percentage = Column(Float,nullable=False)
    cash_tax_rates_avg_money_making_firms_percent = Column(Float,nullable=False)
    cash_tax_rates_aggregate_tax_rate_percentage = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class table_countrytaxrates(Base):
    __tablename__ = "countrytaxrates"
    id = Column(Integer,primary_key=True,nullable=False)
    country = Column(String,nullable=False)
    year_2016_percentage = Column(Float,nullable=False)
    year_2017_percentage = Column(Float,nullable=False)
    year_2018_percentage = Column(Float,nullable=False)
    year_2019_percentage = Column(Float,nullable=False)
    year_2020_percentage = Column(Float,nullable=False)
    year_2021_percentage = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class table_betas(Base):
    __tablename__ = "betas"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms = Column(Integer,nullable=False)
    beta = Column(Float,nullable=False)
    debt_to_equity_ratio_percentage = Column(Float,nullable=False)
    effective_tax_rate_percentage = Column(Float,nullable=False)
    unlevered_beta = Column(Float,nullable=False)
    cash_to_firm_value_percentage = Column(Float,nullable=False)
    unlevered_beta_corrected_for_cash = Column(Float,nullable=False)
    hilo_risk_percentage = Column(Float,nullable=False)
    std_of_equity_percentage = Column(Float,nullable=False)
    std_in_operating_income_last_10_years = Column(Float,nullable=False)
    year_2018 = Column(Float,nullable=False)
    year_2019 = Column(Float,nullable=False)
    year_2020 = Column(Float,nullable=False)
    year_2021 = Column(Float,nullable=False)
    average_2017_22 = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))

class table_histimpl(Base):
    __tablename__ = "histimpl"
    id = Column(Integer,primary_key=True,nullable=False)
    year = Column(Integer,nullable=False)
    earnings_yield_percentage = Column(Float,nullable=False)
    dividend_yield_percentage = Column(Float,nullable=False)
    sp_500 = Column(Float,nullable=False)
    earnings = Column(Float,nullable=False)
    dividends = Column(Float,nullable=False)
    dividends_plus_buybacks = Column(Float,nullable=False)
    change_in_earnings_percentage = Column(Float,nullable=False)
    change_in_dividends_percentage = Column(Float,nullable=False)
    t_bill_rate_percentage = Column(Float,nullable=False)
    t_bond_rate_percentage = Column(Float,nullable=False)
    bond_bill = Column(Float,nullable=False)
    smoothed_growth_percentage = Column(Float,nullable=False)
    implied_premium_ddm_percentage = Column(Float,nullable=False)
    analytst_growth_estimate_percentage = Column(Float,nullable=False)
    impled_erp_for_fcfe_percentage = Column(Float,nullable=False)
    implied_premium_for_fcfe_with_sustainable_payout_percentage = Column(Float,nullable=False)
    erp_riskfree_rate = Column(Float,nullable=False) # ask professor what is that column
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class table_ctryprem(Base):
    __tablename__ = "ctryprem"
    id = Column(Integer,primary_key=True,nullable=False)
    country = Column(String,nullable=False)
    moodys_rating = Column(String,nullable=False)
    adj_default_spread = Column(Float,nullable=False)
    country_risk_premium = Column(Float,nullable=False)
    equity_risk_premium = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))



class table_totalbeta(Base):
    __tablename__ = "totalbeta"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms = Column(Integer,nullable=False)
    average_unlevered_beta = Column(Float,nullable=False)
    average_levered_beta = Column(Float,nullable=False)
    average_correlation_with_market_percentage = Column(Float,nullable=False)
    total_unlevered_beta = Column(Float,nullable=False)
    total_levered_beta = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    


class table_wacc(Base):
    __tablename__ = "wacc"
    id = Column(Integer,primary_key=True,nullable=False)
    industry_name = Column(String,nullable=False)
    number_of_firms = Column(Integer,nullable=False)
    beta = Column(Float,nullable=False)
    cost_of_equity_percentage = Column(Float,nullable=False)
    equity_divided_by_debt_plus_equity_percentage = Column(Float,nullable=False)
    std_dev_in_stock_percentage = Column(Float,nullable=False)
    cost_of_debt_percentage = Column(Float,nullable=False)
    tax_rate_percentage = Column(Float,nullable=False)
    after_tax_cost_of_debt_percentage = Column(Float,nullable=False)
    debt_divided_by_debt_plus_equity_percentage = Column(Float,nullable=False)
    cost_of_capital_percentage = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


    